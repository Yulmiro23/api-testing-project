import requests
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    def get_meme(self, meme_id):
        self.response = requests.get(f'{self.url}/{meme_id}', headers={"Authorization": self.token})
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            self.json = self.response.json()
        else:
            self.json = None
        return self.json
