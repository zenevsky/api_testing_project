import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.meme.models.meme_pydantic_model import DataContainerModel


class GetMemes(Endpoint):

    @allure.step('Run "Get memes" request to get all memes')
    def get_memes(self, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.model = DataContainerModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
