import allure
import requests
import json

from endpoints.endpoint import Endpoint


class CreateAuthorizeToken(Endpoint):

    @allure.step('Run "Create authorize token" request to create new token')
    def create_authorize_token(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=payload,
            headers=headers
        )
        try:
            self.user = self.response.json()['user']
            self.token = self.response.json()['token']
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response

    @allure.step('Check that auth user is the same as in the request')
    def check_auth_user_is_correct(self, user):
        assert self.response.json()['user'] == user
