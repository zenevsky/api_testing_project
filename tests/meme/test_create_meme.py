import allure
import pytest

from endpoints.meme.models.meme_object_model import CreateMemePayload
from helpers.create_meme_test_data import POSITIVE_DATA, NEGATIVE_DATA


@allure.feature('Meme')
@allure.story('Create meme')
class TestCreateMeme:

    @pytest.mark.parametrize('data', POSITIVE_DATA)
    @pytest.mark.critical
    @allure.title('Create meme with valid body')
    def test_create_meme_with_valid_body(self, create_meme_endpoint, delete_meme_endpoint, request, data):
        payload = CreateMemePayload(**data)
        create_meme_endpoint.create_meme(
            payload=payload,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        create_meme_endpoint.check_that_status_is_200()
        create_meme_endpoint.check_user_is_correct(request.config.user)
        create_meme_endpoint.check_response_data(payload)
        delete_meme_endpoint.delete_meme(create_meme_endpoint.model.id)

    @pytest.mark.parametrize('data', NEGATIVE_DATA)
    @pytest.mark.medium
    @allure.title('Create meme with invalid body')
    def test_create_meme_with_invalid_body(self, create_meme_endpoint, request, data):
        payload = CreateMemePayload(**data)
        create_meme_endpoint.create_meme(
            payload=payload,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        create_meme_endpoint.check_that_status_is_400()
        print(create_meme_endpoint.response.status_code)

    @pytest.mark.high
    @allure.title('Create meme without auth')
    def test_create_meme_without_auth(self, create_meme_endpoint):
        create_meme_endpoint.create_meme(payload=CreateMemePayload())
        create_meme_endpoint.check_that_status_is_401()
