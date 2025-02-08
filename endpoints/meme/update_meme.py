import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step('Run "Update meme" request to update meme by id')
    def update_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        return self.response
