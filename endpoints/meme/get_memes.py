import allure
import requests

from endpoints.endpoint import Endpoint


class GetMemes(Endpoint):

    @allure.step('Run "Get memes" request to get all memes')
    def get_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        return self.response
