import allure
import pytest

from helpers.update_meme_test_data import POSITIVE_DATA, NEGATIVE_DATA


@pytest.mark.parametrize('data', POSITIVE_DATA)
@pytest.mark.critical
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update meme with valid body')
def test_update_meme_with_valid_body(meme_id_fixture, update_meme_endpoint, request, data):
    data['id'] = meme_id_fixture
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload=data,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    update_meme_endpoint.check_that_status_is_200()
    update_meme_endpoint.check_user_is_correct(request.config.user)
    update_meme_endpoint.check_text_is_correct(data['text'])
    update_meme_endpoint.check_url_is_correct(data['url'])
    update_meme_endpoint.check_tags_is_correct(data['tags'])
    update_meme_endpoint.check_info_is_correct(data['info'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update meme with invalid body')
def test_update_meme_with_invalid_body(meme_id_fixture, update_meme_endpoint, request, data):
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload=data,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update meme with id in payload that does not match to the path id')
def test_update_meme_with_incorrect_id_in_payload(meme_id_fixture, update_meme_endpoint, request):
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload={"id": 999, "text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    update_meme_endpoint.check_that_status_is_400()


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update meme created by other user')
def test_update_meme_created_by_other_user(meme_id_fixture, update_meme_endpoint, create_authorize_token_endpoint):
    create_authorize_token_endpoint.create_authorize_token(payload={'name': 'another_user'})
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload={"id": meme_id_fixture, "text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': create_authorize_token_endpoint.token}
    )
    update_meme_endpoint.check_that_status_is_403()


@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update deleted meme')
def test_update_deleted_meme(meme_id_fixture, update_meme_endpoint, delete_meme_endpoint, request):
    delete_meme_endpoint.delete_meme(
        meme_id_fixture,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload={"id": meme_id_fixture, "text": "", "url": "", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    update_meme_endpoint.check_that_status_is_404()


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Update memes')
@allure.title('Update meme without auth')
def test_update_meme_without_auth(meme_id_fixture, update_meme_endpoint):
    update_meme_endpoint.update_meme(
        meme_id_fixture,
        payload={"id": meme_id_fixture, "text": "", "url": "", "tags": ["test"], "info": {"test": "test"}})
    update_meme_endpoint.check_that_status_is_401()
