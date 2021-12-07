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

    def _get_encounter_fights(self) -> dict:
        query = f'''{{ 
                reportData {{
                    report (code: "{self.report_id}") {{
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
            return r.json()['data']['reportData']['report']['fights']
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

        r = self.api.query(query)

        if r.status_code == 200:
            return r.json()['data']['reportData']['report']['events']['data']
        else:
            raise RuntimeError(api_error_msg(self.get_debuff_events.__name__, r))

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

        r = self.api.query(query)

        if r.status_code == 200:
            return r.json()['data']['reportData']['report']['events']['data']
        else:
            raise RuntimeError(api_error_msg(self.get_debuff_events.__name__, r))


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
        fights = self._get_encounter_fights()

        print(f'**Time it takes for the core to be picked up and dunked for report {self.report_id}**')
        print('cores passed less than two times are considered lost')

        for x in range(0, len(fights)):
            tainted_core_debuff_events = self.get_debuff_events(tainted_core_debuff_id, fights[x]['startTime'],
                                                                fights[x]['endTime'])
            timings = self.core_timings(tainted_core_debuff_events)

            print(f'\n*Vashj attempt #{x + 1}*')

            for y in range(0, len(timings)):
                if timings[y]:
                    print(f'{y + 1}. took {timings[y]} sec')
                else:
                    print(f'{y + 1}. core lost to player death?')

            print(f'See https://tbc.warcraftlogs.com/reports/{self.report_id}#fight={fights[x]["id"]}'
                  f'&type=auras&spells=debuffs&ability={tainted_core_debuff_id}&view=events')

    def tainted_elemental_stats(self, tainted_count: int, damage_taken_events: list[dict]):
        result = []

        for n in range(1, tainted_count + 1):
            events = [e for e in damage_taken_events if e['targetInstance'] == n]

            if events:
                damage_taken = sum([e['amount'] for e in events])
                duration = self._time_between(events[0]['timestamp'], events[-1]['timestamp'])
                killed = True in ['overkill' in e for e in events]
            else:
                damage_taken = 0
                duration = None
                killed = False

            result.append({
                'damage': damage_taken,
                'duration': duration,
                'killed': killed
            })

        return result

    def print_tainted_elemental_damage_taken(self):
        tainted_game_id = 22009
        fights = self._get_encounter_fights()

        print(f'**Damage done to Tainted Elementals for report {self.report_id}**')

        for x in range(0, len(fights)):
            # get number of spawned Tainted Elementals and their reportID
            tainted_elementals = list(filter(lambda c: c['gameID'] == tainted_game_id, fights[x]['enemyNPCs']))[0]

            events = self.get_enemy_damage_taken(tainted_elementals['id'], fights[x]['startTime'], fights[x]['endTime'])
            stats = self.tainted_elemental_stats(tainted_elementals['instanceCount'], events)

            print(f'\n*Vashj attempt #{x + 1}*')

            for y in range(0, len(stats)):
                rip = 'died' if stats[y]['killed'] else 'despawned'

                if stats[y]['duration']:
                    print(f'{y + 1}. took {stats[y]["damage"]} damage over {stats[y]["duration"]} seconds and {rip}.')
                else:
                    print(f'{y + 1}. took {stats[y]["damage"]} and {rip}')

            print(f'See https://tbc.warcraftlogs.com/reports/{self.report_id}#fight={fights[x]["id"]}'
                  f'&type=damage-taken&hostility=1&source={tainted_elementals["id"]}&view=events')
