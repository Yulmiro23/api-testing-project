import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, obj_id):
        self.response = requests.delete(f'{self.url}/{obj_id}', headers={"Authorization": self.token})
        return self.response.status_code
