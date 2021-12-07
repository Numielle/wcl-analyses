from warcraftlogs.analysers import VashjAnalyser
from warcraftlogs.api import WarcraftLogsAPI

if __name__ == '__main__':
    report_id = '79qk2H4jCMZTAfwP'  # last PdH SSC
    at = None
    at = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NTA4MTA4Ni1jNDc3LTQ5NzMtOTRlYS05MWQwOWU3ZTRhMjkiLCJqdGkiOiJlYWIzNDFjNmIyNDlkZTlhOTMyNzljMWY3ZGU2OGJkNDMwYmE0M2M5YzY4MGQwMWFmZmE5NzNhOGQ4MGQxZDI3N2VkNjZjZWY4YTE5MDViZCIsImlhdCI6MTYzODcwMjk2MCwibmJmIjoxNjM4NzAyOTYwLCJleHAiOjE2NDkwNzA5NjAsInN1YiI6IiIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.B8DIcndI9KN4piNHa-5OKFbtAPnadyotBcb1hEmJ4nEmKSudhoSJonyf9mlaGvf7woQWsV8S6n89kROwjTL4ER9KgcfNZN0vvsTSoRNQf3CgkqUYIcAhyOrK9IZvZ0d7hunnY3iVlnlL3Jn6f5sCSXMvkvLZfBbkS2r4ypMnAcYIgFytf5i9u71XM2orFuae-wo2LMmP9pTVjPefw-nSttSx27WBimBGXp0PF8WVtSj_CTa7H1hSudZySCqXsxv05dBvs0G4XC1FGEIUcsLAJtXlazh3o23hR8tDUF53OLgjP8IjVP009Nnq1pFhY_O7pxyrh1CTcj9NwYOZRES0CsnKR0-PS8RukwPCtoAeS9ZaO-sB3z42iWXzIHP_j_dvSiTCG7fxDo-JuLzVN2eX3jfuyfUusdthe3-rHBS1ciTg-cDPTn9vFw8yztmyIV3g3BkctFo0FNNdVIrG8d23IKKKTzMbZgvLTcNbbnhT2gEklO2GJ42L7-3L6rAjPQxpTZYFvb-8yyaMhF5FblVQCEirGWWow-gXgC6xXPAmgvYSZgx2_1xgEWo0MC7ZmZlxA8MaL4XMbnJiAJIMNDvjseybF1FNZDdmFpiLbV9MjO6rsLl1A-tiKcGHcBN0wNRXWQs9gS5S6SK2rbKGE7oysneqEfMsqzY-MPi-JWgrwPE'
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
