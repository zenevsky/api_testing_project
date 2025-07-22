import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.meme.models.meme_pydantic_model import MemeModel


class GetMeme(Endpoint):

    @allure.step('Run "Get meme" request to get meme by id')
    def get_meme(self, meme_id, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.model = MemeModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
