import json

import allure
import requests
from requests import Response
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from endpoints.authorize.models.auth_pydantic_model import AuthorizeModel
from endpoints.endpoint import Endpoint


class GetAuthorizeToken(Endpoint):

    @allure.step('Run "Get authorize token" request to get token')
    def get_authorize_token(self, token, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/authorize/{token}',
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.model = AuthorizeModel(**self.json)
        except json.JSONDecodeError:
            pass
        return self.response

    @allure.step('Check that auth user is the same as in the request')
    def check_auth_user_is_correct(self, user):
        user_from_response = self.response.text.split('Username is ')[-1]
        assert user_from_response == user

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_fixed(3),
        retry=retry_if_exception_type(AssertionError),
        reraise=True
    )
    @allure.step('Check that 404 error received (with retry)')
    def get_authorize_token_and_check_that_status_is_404(self, token):
        self.get_authorize_token(token)
        assert self.response.status_code == 404, (
            f"Expected status 404, but got {self.response.status_code}. "
            f"Response: {self.response.text}"
        )
