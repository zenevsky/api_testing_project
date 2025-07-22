import allure
import pydantic
import requests

from endpoints.authorize.models.auth_pydantic_model import KillAuthModel
from endpoints.endpoint import Endpoint


class KillAuthorizeToken(Endpoint):

    @allure.step('Run "Kill authorize token" request to kill token')
    def kill_authorize_token(self, token, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/authorize/kill/{token}',
            headers=headers
        )
        try:
            self.model = KillAuthModel()
        except pydantic.ValidationError:
            pass
        return self.response
