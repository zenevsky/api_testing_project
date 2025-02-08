import allure
import pytest


@pytest.mark.critical
@allure.feature('Meme')
@allure.story('Get meme')
@allure.title('Get meme with auth')
def test_get_meme_with_auth(get_meme_endpoint, request, meme_id_fixture):
    get_meme_endpoint.get_meme(
        meme_id_fixture,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    get_meme_endpoint.check_that_status_is_200()
    get_meme_endpoint.check_id_is_correct(meme_id_fixture)


@pytest.mark.high
@allure.feature('Meme')
@allure.story('Get meme')
@allure.title('Get meme without auth')
def test_get_meme_without_auth(get_meme_endpoint, meme_id_fixture):
    get_meme_endpoint.get_meme(meme_id_fixture)
    get_meme_endpoint.check_that_status_is_401()


@pytest.mark.medium
@allure.feature('Meme')
@allure.story('Get meme')
@allure.title('Get not existing meme')
def test_get_not_existing_meme(get_meme_endpoint, delete_meme_endpoint, request, meme_id_fixture):
    delete_meme_endpoint.delete_meme(
        meme_id_fixture,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    get_meme_endpoint.get_meme(
        meme_id_fixture,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    get_meme_endpoint.check_that_status_is_404()
