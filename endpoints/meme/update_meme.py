import allure
import requests
import json

from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.meme.models.meme_pydantic_model import MemeModel
from endpoints.meme.models.meme_object_model import UpdateMemePayload


class UpdateMeme(Endpoint):

    @allure.step('Run "Update meme" request to update meme by id')
    def update_meme(self, meme_id, payload: UpdateMemePayload, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.model = MemeModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
