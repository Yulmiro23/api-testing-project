import requests
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

    def put_meme(self, meme_id, data):
        self.response = requests.put(f'{self.url}/{meme_id}', headers={"Authorization": self.token}, json=data)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            self.json = self.response.json()
        else:
            self.json = None
        return self.json


    def check_put(self, data):
        assert self.json['info'] == data['info']
