class Endpoint:
    url = 'http://167.172.172.115:52355/meme'
    token = None
    response = None
    json = None


    def check_status_code(self):
        assert self.response.status_code == 200, 'Error: not 200'


    def check_id(self, meme_id):
        assert self.json['id'] == meme_id, 'Error: wrong id'


    def check_not_found(self):
        assert self.response.status_code == 404, 'Error: not 404'


    def check_not_unauthorized(self):
        assert self.response.status_code == 401, 'Error: not 401'


    def check_bad_request(self):
        assert self.response.status_code == 400, 'Error: not 400'


    def check_forbidden(self):
        assert self.response.status_code == 403, 'Error: not 403'
