import allure
import pytest

from helpers.create_meme_test_data import POSITIVE_DATA, NEGATIVE_DATA


@pytest.mark.parametrize('data', POSITIVE_DATA)
@pytest.mark.critical
@allure.feature('Meme')
@allure.story('Create meme')
@allure.title('Create meme with valid body')
def test_create_meme_with_valid_body(create_meme_endpoint, delete_meme_endpoint, request, data):
    create_meme_endpoint.create_meme(
        payload=data,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_user_is_correct(request.config.user)
    create_meme_endpoint.check_text_is_correct(data['text'])
    create_meme_endpoint.check_url_is_correct(data['url'])
    create_meme_endpoint.check_tags_is_correct(data['tags'])
    create_meme_endpoint.check_info_is_correct(data['info'])
    delete_meme_endpoint.delete_meme(create_meme_endpoint.meme_id)


@pytest.mark.parametrize('data', NEGATIVE_DATA)
@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Create meme')
@allure.title('Create meme with invalid body')
def test_create_meme_with_invalid_body(create_meme_endpoint, request, data):
    create_meme_endpoint.create_meme(
        payload=data,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    create_meme_endpoint.check_that_status_is_400()


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Create meme')
@allure.title('Create meme without auth')
def test_create_meme_without_auth(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload={"text": "", "url": "", "tags": ["test"], "info": {"test": "test"}})
    create_meme_endpoint.check_that_status_is_401()
