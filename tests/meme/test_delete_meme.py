import allure
import pytest

from endpoints.authorize.models.auth_object_model import AuthorizePayload
from endpoints.meme.models.meme_object_model import CreateMemePayload


@allure.feature('Meme')
@allure.story('Delete meme')
class TestDeleteMeme:

    @pytest.mark.critical
    @allure.title('Delete existing meme')
    def test_delete_existing_meme(self, create_meme_endpoint, delete_meme_endpoint, get_meme_endpoint,
                                  create_meme_payload, request):
        create_meme_endpoint.create_meme(
            payload=CreateMemePayload(),
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        delete_meme_endpoint.delete_meme(
            create_meme_endpoint.model.id,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        delete_meme_endpoint.check_that_status_is_200()
        get_meme_endpoint.get_meme(
            create_meme_endpoint.model.id,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )

    @pytest.mark.medium
    @allure.title('Delete not existing meme')
    def test_delete_not_existing_meme(self, create_meme_endpoint, delete_meme_endpoint, request):
        create_meme_endpoint.create_meme(
            payload=CreateMemePayload(),
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        delete_meme_endpoint.delete_meme(
            create_meme_endpoint.model.id,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        delete_meme_endpoint.delete_meme(
            create_meme_endpoint.model.id,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )
        delete_meme_endpoint.check_that_status_is_404()

    @pytest.mark.high
    @allure.title('Delete meme created by other user')
    def test_delete_meme_created_by_another_user(self, meme_id_fixture, create_authorize_token_endpoint,
                                                 delete_meme_endpoint, get_meme_endpoint, request):
        create_authorize_token_endpoint.create_authorize_token(
            payload=AuthorizePayload(name='another_user')
        )
        delete_meme_endpoint.delete_meme(
            meme_id_fixture,
            headers={'Content-type': 'application/json', 'Authorization': create_authorize_token_endpoint.model.token}
        )
        delete_meme_endpoint.check_that_status_is_403()
        get_meme_endpoint.get_meme(
            meme_id_fixture,
            headers={'Content-type': 'application/json', 'Authorization': request.config.token}
        )

    @pytest.mark.high
    @allure.title('Delete meme without auth')
    def test_delete_meme_without_auth(self, meme_id_fixture, delete_meme_endpoint):
        delete_meme_endpoint.delete_meme(meme_id_fixture)
        delete_meme_endpoint.check_that_status_is_401()
