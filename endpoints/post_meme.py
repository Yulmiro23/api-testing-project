import requests
from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):

    def create_meme(self, data):
        self.response = requests.post(self.url, headers={"Authorization": self.token}, json=data)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            self.json = self.response.json()
        else:
            self.json = None
        return self.json
