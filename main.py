import os

from warcraftlogs.analysers import VashjAnalyser, KaelthasAnalyser
from warcraftlogs.api import WarcraftLogsAPI

import click


@click.command()
@click.argument('report_id')
def main(report_id):
    at = os.environ.get('AT', default=None)
    api = WarcraftLogsAPI(at)
    v = VashjAnalyser(api, report_id)
    v.full_report()

    kt = KaelthasAnalyser(api, report_id)
    kt.print_phoenix_egg_uptime()


if __name__ == '__main__':
    main()
