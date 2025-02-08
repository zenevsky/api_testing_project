import allure


class Endpoint:
    url = 'http://167.172.172.115:52355/'
    response = None
    json = None
    token = None
    user = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400

    @allure.step('Check that response is 401')
    def check_that_status_is_401(self):
        assert self.response.status_code == 401

    @allure.step('Check that response is 403')
    def check_that_status_is_403(self):
        assert self.response.status_code == 403

    @allure.step('Check that 404 error received')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404

    @allure.step('Check that id is correct')
    def check_id_is_correct(self, meme_id):
        assert self.response.json()['id'] == meme_id

    @allure.step('Check that user is correct')
    def check_user_is_correct(self, user):
        assert self.response.json()['updated_by'] == user

    @allure.step('Check that text is the same as in the request')
    def check_text_is_correct(self, text):
        assert self.response.json()['text'] == text

    @allure.step('Check that url is the same as in the request')
    def check_url_is_correct(self, url):
        assert self.response.json()['url'] == url

    @allure.step('Check that tags is the same as in the request')
    def check_tags_is_correct(self, tags):
        assert self.response.json()['tags'] == tags

    @allure.step('Check that info is the same as in the request')
    def check_info_is_correct(self, info):
        assert self.response.json()['info'] == info
