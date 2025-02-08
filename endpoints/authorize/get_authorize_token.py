import allure
import requests

from endpoints.endpoint import Endpoint


class GetAuthorizeToken(Endpoint):

    @allure.step('Run "Get authorize token" request to get token')
    def get_authorize_token(self, token, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/authorize/{token}',
            headers=headers
        )
        return self.response

    @allure.step('Check that auth user is the same as in the request')
    def check_auth_user_is_correct(self, user):
        user_from_response = self.response.text.split('Username is ')[-1]
        assert user_from_response == user
