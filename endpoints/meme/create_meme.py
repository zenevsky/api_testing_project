import allure
import requests
import json

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None
    meme_text = None
    meme_url = None
    meme_tags = None
    meme_info = None
    meme_updated_by = None

    @allure.step('Run "Create meme" request to create new meme')
    def create_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.meme_id = self.json['id']
            self.meme_text = self.json['text']
            self.meme_url = self.json['url']
            self.meme_tags = self.json['tags']
            self.meme_info = self.json['info']
            self.meme_updated_by = self.response.json()['updated_by']
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
