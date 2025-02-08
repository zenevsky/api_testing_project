import allure
import pytest

from conftest import create_authorize_token_endpoint


@pytest.mark.critical
@allure.feature('Meme')
@allure.story('Delete meme')
@allure.title('Delete existing meme')
def test_delete_existing_meme(create_meme_endpoint, delete_meme_endpoint, request):
    create_meme_endpoint.create_meme(
        payload={"text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.delete_meme(
        create_meme_endpoint.meme_id,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.check_that_status_is_200()


@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Delete meme')
@allure.title('Delete not existing meme')
def test_delete_not_existing_meme(create_meme_endpoint, delete_meme_endpoint, request):
    create_meme_endpoint.create_meme(
        payload={"text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.delete_meme(
        create_meme_endpoint.meme_id,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.delete_meme(
        create_meme_endpoint.meme_id,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.check_that_status_is_404()


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Delete meme')
@allure.title('Delete meme created by other user')
def test_delete_meme_created_by_another_user(create_meme_endpoint, create_authorize_token_endpoint,
                                             delete_meme_endpoint, request):
    create_meme_endpoint.create_meme(
        payload={"text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    create_authorize_token_endpoint.create_authorize_token(payload={'name': 'another_user'})
    delete_meme_endpoint.delete_meme(
        create_meme_endpoint.meme_id,
        headers={'Content-type': 'application/json', 'Authorization': create_authorize_token_endpoint.token}
    )
    delete_meme_endpoint.check_that_status_is_403()


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Delete meme')
@allure.title('Delete meme without auth')
def test_delete_meme_without_auth(create_meme_endpoint, delete_meme_endpoint, request):
    create_meme_endpoint.create_meme(
        payload={"text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    delete_meme_endpoint.delete_meme(create_meme_endpoint.meme_id)
    delete_meme_endpoint.check_that_status_is_401()
