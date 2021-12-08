from typing import Callable

from warcraftlogs.api import WarcraftLogsAPI
from warcraftlogs.utils import api_error_msg


class FightAnalyser:
    def __init__(self, api: WarcraftLogsAPI, report_id: str, encounter_id: int):
        self.api = api
        self.report_id = report_id
        self.encounter_id = encounter_id

    @staticmethod
    def _time_between(start_time, end_time):
        return round((end_time - start_time) / 1000, 1)

    def _get_encounter_fights(self) -> tuple[list[dict], list[dict]]:
        query = f'''{{ 
                reportData {{
                    report (code: "{self.report_id}") {{
                        masterData {{
                            actors {{
                                id
                                name
                                petOwner
                            }}
                        }}
                        fights (encounterID: {self.encounter_id}) {{
                            id
                            name
                            fightPercentage
                            startTime
                            endTime
                            enemyNPCs {{
                                gameID
                                id
                                instanceCount
                                groupCount
                            }}
                        }}
                    }}
                }} 
                }}'''
        r = self.api.query(query)

        if r.status_code == 200:
            return r.json()['data']['reportData']['report']['fights'], \
                   r.json()['data']['reportData']['report']['masterData']['actors']
        else:
            raise RuntimeError(api_error_msg(self._get_encounter_fights.__name__, r))

    def get_debuff_events(self, ability_id: int, start_time: int, end_time: int):
        query = f'''{{
        reportData {{
            report (code: "{self.report_id}") {{
                events (dataType: Debuffs, abilityID: {ability_id}, startTime: {start_time}, endTime: {end_time}) {{
                    data
                    nextPageTimestamp
                }}
            }}
        }}
        }}'''

        return self.api.query_all_event_pages(query)

    def get_enemy_damage_taken(self, enemy_id: int, start_time: int, end_time: int):
        query = f'''{{
        reportData {{
            report (code: "{self.report_id}") {{
                events (dataType: DamageTaken, sourceID: {enemy_id}, hostilityType: Enemies, startTime: {start_time}, endTime: {end_time}) {{
                    data
                    nextPageTimestamp
                }}
            }}
        }}
        }}'''

        return self.api.query_all_event_pages(query)

    def enemy_uptime_damage_taken(self, enemy_count: int, damage_taken_events: list[dict]):
        result = []

        for n in range(1, enemy_count + 1):
            events = self.get_events_for_target_instance(damage_taken_events, enemy_count, n)

            attackers = set([e['sourceID'] for e in events])

            if events:
                # calculate total amount and duration of damage dealt to enemy
                damage_taken = sum([e['amount'] for e in events])
                first_attack = events[0]['timestamp']
                last_attack = events[-1]['timestamp']
                duration = self._time_between(first_attack, last_attack)
                killed = True in ['overkill' in e for e in events]
                # calculate who dealt how much damage to enemy
                distribution = []
                for a in attackers:
                    damage = sum([e['amount'] for e in events if e['sourceID'] == a])
                    percent = round(damage / damage_taken * 100, 1)
                    distribution.append((a, damage, percent))
                distribution.sort(key=lambda x: x[1], reverse=True)
            else:
                damage_taken = 0
                first_attack = None
                last_attack = None
                duration = None
                killed = False
                distribution = []

            result.append({
                'damage': damage_taken,
                'first_attack': first_attack,
                'last_attack': last_attack,
                'duration': duration,
                'killed': killed,
                'distribution': distribution
            })

        return result

    def get_events_for_target_instance(self, damage_taken_events, enemy_count, target_instance):
        if enemy_count > 1:
            events = [e for e in damage_taken_events if e['targetInstance'] == target_instance]
        else:
            # targetInstance not set if mob is unique
            events = damage_taken_events
        return events

    @staticmethod
    def _convert_actors_to_dict(actors: list[dict]):
        result = {}
        for entry in actors:
            result[entry['id']] = {
                'name': entry['name'],
                'petOwner': entry['petOwner']
            }

        return result

    def print_enemy_uptime(self, enemy_game_id: int, enemy_name: str, not_dead_text: str = ''):
        fights, actor_names = self._get_encounter_fights()
        actor_names = self._convert_actors_to_dict(actor_names)

        print(f'**Damage done to {enemy_name} for report {self.report_id}**')

        for x in range(0, len(fights)):
            print(f'\n*{fights[x]["name"]} attempt #{x + 1}*')

            try:
                # get number of spawned enemy and their reportID
                enemies = list(filter(lambda c: c['gameID'] == enemy_game_id, fights[x]['enemyNPCs']))[0]
            except IndexError:
                # enemy didn't spawn this attempt
                continue

            events = self.get_enemy_damage_taken(enemies['id'], fights[x]['startTime'], fights[x]['endTime'])
            stats = self.enemy_uptime_damage_taken(enemies['instanceCount'], events)

            for y in range(0, len(stats)):
                rip = ' and died' if stats[y]['killed'] else not_dead_text

                if stats[y]['duration']:
                    print(f'\n{y + 1}. {enemy_name} took {stats[y]["damage"]} damage '
                          f'over {stats[y]["duration"]} seconds{rip}.')
                    url_source_id = f'{enemies["id"]}.{y + 1}' if enemies['instanceCount'] > 1 else enemies['id']

                    link = f'https://classic.warcraftlogs.com/reports/{self.report_id}#fight={fights[x]["id"]}'\
                           f'&type=damage-taken&hostility=1&source={url_source_id}&start={stats[y]["first_attack"]}'\
                           f'&end={stats[y]["last_attack"]}&by=target'

                    print(f'    Damage done: {link}')
                    print(f'    Timeline:    {link}&view=timeline')

                    # resolve actor IDs to actor names and print damage distribution
                    for actor in stats[y]['distribution']:
                        actor_owner_id = actor_names[actor[0]]['petOwner']

                        if actor_owner_id:
                            name = f'{actor_names[actor[0]]["name"]} ({actor_names[actor_owner_id]["name"]})'
                        else:
                            name = actor_names[actor[0]]['name']
                        # TODO do we need this?
                        # print(f'  {name} dealt {actor[1]} damage to {enemy_name} {y + 1} ({actor[2]}%).')
                else:
                    print(f'\n{y + 1}. {enemy_name} took {stats[y]["damage"]} damage.')

            # print(f'\nSee https://tbc.warcraftlogs.com/reports/{self.report_id}#fight={fights[x]["id"]}'
            #       f'&type=damage-taken&hostility=1&source={enemies["id"]}&view=events')

    def full_report(self, functions: list[Callable]):
        for f in functions:
            f()
            print()
            print()


class VashjAnalyser(FightAnalyser):
    def __init__(self, api: WarcraftLogsAPI, report_id):
        super().__init__(api, report_id, 628)

    def core_timings(self, tainted_core_debuff_events: list[dict]):
        result = []

        if not len(tainted_core_debuff_events):
            return result

        pickup_time = tainted_core_debuff_events[0]['timestamp']
        passes = 0

        for n in range(2, len(tainted_core_debuff_events), 2):
            # calculate 'flight time' as difference between current debuff gain and previous debuff drop off
            flight_time = tainted_core_debuff_events[n]['timestamp'] - tainted_core_debuff_events[n - 1]['timestamp']

            # assumption: if the 'flight time' of a core is longer than 2 seconds, it's the next core
            if flight_time > 2000:
                # assumption: if core wasn't passed at least two times, then the core carrier died
                if passes < 2:
                    result.append(None)
                else:
                    result.append(self._time_between(pickup_time, tainted_core_debuff_events[n - 1]['timestamp']))

                pickup_time = tainted_core_debuff_events[n]['timestamp']
                passes = 0
            else:
                passes = passes + 1

        # add last core time as well
        if passes < 2:
            result.append(None)
        else:
            result.append(self._time_between(pickup_time, tainted_core_debuff_events[-1]['timestamp']))

        return result

    def print_core_dunk_times(self):
        tainted_core_debuff_id = 38132
        fights, actor_names = self._get_encounter_fights()

        print(f'**Time it takes for the core to be picked up and dunked for report {self.report_id}**')
        print('cores passed less than two times are considered lost')

        for x in range(0, len(fights)):
            tainted_core_debuff_events = self.get_debuff_events(tainted_core_debuff_id, fights[x]['startTime'],
                                                                fights[x]['endTime'])
            timings = self.core_timings(tainted_core_debuff_events)

            print(f'\n*{fights[x]["name"]} attempt #{x + 1}*')

            for y in range(0, len(timings)):
                if timings[y]:
                    print(f'{y + 1}. core took {timings[y]} sec')
                else:
                    print(f'{y + 1}. core lost to player death?')

            print(f'See https://tbc.warcraftlogs.com/reports/{self.report_id}#fight={fights[x]["id"]}'
                  f'&type=auras&spells=debuffs&ability={tainted_core_debuff_id}&view=events')

    def print_strider_uptime(self):
        self.print_enemy_uptime(22056, 'Coilfang Strider')

    def print_tainted_uptime(self):
        self.print_enemy_uptime(22009, 'Tainted Elemental', not_dead_text=' and despawned')

    def full_report(self):
        super().full_report([self.print_core_dunk_times, self.print_tainted_uptime, self.print_strider_uptime])


class KaelthasAnalyser(FightAnalyser):
    def __init__(self, api: WarcraftLogsAPI, report_id):
        super().__init__(api, report_id, 733)

    def print_phoenix_egg_uptime(self):
        self.print_enemy_uptime(21364, 'Phoenix Egg', not_dead_text=' and hatched')
