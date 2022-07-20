import requests
import logging

TEMPO_URL = 'https://api.tempo.io/4'

def urljoin(base, path):
    return base + path

class Tempo:
    def __init__(self, token, account_id, logging_level=logging.INFO):
        self.header = {
            "Authorization": f"Bearer {token}"
        }
        self.account_id = account_id
        self.baseUrl = TEMPO_URL
        self.session = requests.Session()
        self.session.headers.update(self.header)
        self.logging_level = logging_level

    def __api_post(self, path, data=None, headers=None, params=None, json=None, raise_for_status=True):
        logging.getLogger("tempo").setLevel(self.logging_level)
        url = urljoin(self.baseUrl, path)
        response = self.session.post(url, data=data, headers=headers, params=params, json=json, timeout=3)
        if raise_for_status:
            response.raise_for_status()
        logging.debug('post')
        return response.json()

    def post_worklog(self, issue_key, date, time):
        payload = {
            "authorAccountId": self.account_id,
            "issueKey": issue_key,
            "startDate": date,
            "timeSpentSeconds": time,
            "description": "Tempo cli tool"
        }

        return self.__api_post('/worklogs', json=payload)

