import json

import requests
from requests import Response
from requests.structures import CaseInsensitiveDict

from warcraftlogs.utils import api_error_msg


class WarcraftLogsAPI:
    def __init__(self, access_token: str = None):
        self.public_api = 'https://classic.warcraftlogs.com/api/v2/client'
        self.private_api = 'https://classic.warcraftlogs.com/api/v2/user'

        if access_token:
            self.access_token = access_token
        else:
            cred = self.load_credentials()
            self.access_token = self.get_access_token(cred['client_id'], cred['client_secret'])

    def query(self, query: str) -> Response:
        headers = CaseInsensitiveDict()
        headers['Accept'] = 'application/json'
        headers['Authorization'] = f'Bearer {self.access_token}'

        return requests.post(self.public_api, json={'query': query}, headers=headers)

    @staticmethod
    def load_credentials(filename: str = 'credentials.json') -> dict[str, str]:
        with open(filename) as json_file:
            return json.load(json_file)

    def get_access_token(self, client_id: str, client_secret: str):
        r = requests.post('https://classic.warcraftlogs.com/oauth/token',
                          data={'grant_type': 'client_credentials'},
                          auth=(client_id, client_secret))

        if r.status_code == 200:
            return r.json()['access_token']
        else:
            raise RuntimeError(api_error_msg(self.get_access_token.__name__, r))
