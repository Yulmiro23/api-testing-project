import requests
import os


class Authorization:
    url = 'http://167.172.172.115:52355/authorize'
    body = {"name": "cheburek"}
    path = os.path.dirname(__file__)
    file_path = os.path.dirname(path)
    token_file = os.path.join(file_path, 'token.txt')


    def write_token(self, token):
        with open(self.token_file, 'w') as token_file:
            token_file.write(token)


    def generate_token(self):
        response = requests.post(self.url, json=self.body).json()
        return response["token"]


    def check_file(self):
        if os.path.isfile(self.token_file):
            with open(self.token_file, 'r') as token_file:
                token = token_file.readline()
        else:
            token = None
        return token


    def check_token(self, token):
        response = requests.get(f'{self.url}/{token}')
        return response.status_code == 200
