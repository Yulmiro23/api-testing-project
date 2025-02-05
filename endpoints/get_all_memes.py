import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    def get_memes(self):
        self.response = requests.get(self.url, headers={"Authorization": self.token})
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            self.json = self.response.json()
        else:
            self.json = None
        return self.json
