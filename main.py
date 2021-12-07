from warcraftlogs.analysers import VashjAnalyser
from warcraftlogs.api import WarcraftLogsAPI

if __name__ == '__main__':
    report_id = '79qk2H4jCMZTAfwP'  # last PdH SSC
    at = None
    api = WarcraftLogsAPI(at)
    v = VashjAnalyser(api, report_id)
    v.print_core_dunk_times()
    print()
    print()
    # v.print_tainted_elemental_damage_taken()
    v.print_tainted_uptime()
    print()
    print()
    v.print_strider_uptime()
    print()
