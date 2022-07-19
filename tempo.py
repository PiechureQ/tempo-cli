import requests

class Tempo:
    def __init__(self, token, url):
        self.header = {
            "Authorization": f"Bearer {token}"
        }
        self.baseUrl = url
        self.session = requests.Session()
        self.session.headers.update(self.header)

    def test(self):
        print('Tempo class test')
