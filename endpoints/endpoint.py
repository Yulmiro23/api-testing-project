class Endpoint:
    url = 'http://167.172.172.115:52355/meme'
    token = None
    response = None
    json = None


    def assert_status_200(self):
        assert self.response.status_code == 200, 'Error: not 200'


    def check_id(self, meme_id):
        assert self.json['id'] == meme_id, 'Error: wrong id'


    def assert_status_404(self):
        assert self.response.status_code == 404, 'Error: not 404'


    def assert_status_401(self):
        assert self.response.status_code == 401, 'Error: not 401'


    def assert_status_400(self):
        assert self.response.status_code == 400, 'Error: not 400'


    def assert_status_403(self):
        assert self.response.status_code == 403, 'Error: not 403'
