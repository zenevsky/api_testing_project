import allure
import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.step('Run "Get meme" request to get meme by id')
    def get_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        return self.response
