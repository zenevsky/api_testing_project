from typing import Union, Dict, Any

import allure
import requests
import json

from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.authorize.models.auth_pydantic_model import AuthorizeModel
from endpoints.authorize.models.auth_object_model import AuthorizePayload


class CreateAuthorizeToken(Endpoint):

    @allure.step('Run "Create authorize token" request to create new token')
    def create_authorize_token(self, payload: Union[AuthorizePayload, Dict[str, Any]], headers=None) -> Response:

        payload_dict = payload.to_dict() if isinstance(payload, AuthorizePayload) else payload
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=payload_dict,
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
        assert self.model.user == user
