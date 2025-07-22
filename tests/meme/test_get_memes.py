import allure
import pytest


@allure.feature('Meme')
@allure.story('Get memes')
class TestGetMemes:

    @pytest.mark.critical
    @allure.title('Get memes with auth')
    def test_get_memes(self, get_memes_endpoint, request):
        get_memes_endpoint.get_memes(
            headers={'Content-type': 'application/json', 'Authorization': request.config.token})
        get_memes_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Get memes without auth')
    def test_get_memes_without_auth(self, get_memes_endpoint):
        get_memes_endpoint.get_memes()
        get_memes_endpoint.check_that_status_is_401()
