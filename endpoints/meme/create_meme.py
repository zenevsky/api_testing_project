import allure
import requests
import json

from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.meme.models.meme_pydantic_model import MemeModel
from endpoints.meme.models.meme_object_model import CreateMemePayload


class CreateMeme(Endpoint):

    @allure.step('Run "Create meme" request to create new meme')
    def create_meme(self, payload: CreateMemePayload, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.model = MemeModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
