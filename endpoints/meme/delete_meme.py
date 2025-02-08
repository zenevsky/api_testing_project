import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Run "Delete meme" request to get meme by id')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        return self.response
