import allure
import pytest

from helpers.update_meme_test_data import POSITIVE_DATA, NEGATIVE_DATA
from endpoints.meme.models.meme_object_model import UpdateMemePayload


@allure.feature('Meme')
@allure.story('Update memes')
class TestUpdateMeme:

    @pytest.mark.parametrize('data', POSITIVE_DATA)
    @pytest.mark.critical
    @allure.title('Update meme with valid body')
    def test_update_meme_with_valid_body(self, meme_id_fixture, update_meme_endpoint, request, data):
        data['id'] = meme_id_fixture
        payload = UpdateMemePayload(**data)
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=payload,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        update_meme_endpoint.check_that_status_is_200()
        update_meme_endpoint.check_user_is_correct(request.config.user)
        update_meme_endpoint.check_response_data(payload)

    @pytest.mark.parametrize('data', NEGATIVE_DATA)
    @pytest.mark.medium
    @allure.title('Update meme with invalid body')
    def test_update_meme_with_invalid_body(self, meme_id_fixture, update_meme_endpoint, request, data):
        payload = UpdateMemePayload(**data)
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=payload,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        update_meme_endpoint.check_that_status_is_400()

    @pytest.mark.medium
    @allure.title('Update meme with id in payload that does not match to the path id')
    def test_update_meme_with_incorrect_id_in_payload(self, meme_id_fixture, update_meme_endpoint, request):
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=UpdateMemePayload(),
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        update_meme_endpoint.check_that_status_is_400()

    @pytest.mark.high
    @allure.title('Update meme created by other user')
    def test_update_meme_created_by_other_user(self, meme_id_fixture, update_meme_endpoint,
                                               create_authorize_token_endpoint):
        create_authorize_token_endpoint.create_authorize_token(payload={'name': 'another_user'})
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=UpdateMemePayload(id=meme_id_fixture),
            headers={'Content-type': 'application/json', 'Authorization': create_authorize_token_endpoint.model.token}
        )
        update_meme_endpoint.check_that_status_is_403()

    @pytest.mark.medium
    @allure.title('Update deleted meme')
    def test_update_deleted_meme(self, meme_id_fixture, update_meme_endpoint, delete_meme_endpoint, request):
        delete_meme_endpoint.delete_meme(
            meme_id_fixture,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=UpdateMemePayload(id=meme_id_fixture),
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        update_meme_endpoint.check_that_status_is_404()

    @pytest.mark.high
    @allure.title('Update meme without auth')
    def test_update_meme_without_auth(self, meme_id_fixture, update_meme_endpoint):
        update_meme_endpoint.update_meme(
            meme_id_fixture,
            payload=UpdateMemePayload(id=meme_id_fixture)
        )
        update_meme_endpoint.check_that_status_is_401()
