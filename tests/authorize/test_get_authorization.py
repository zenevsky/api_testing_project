import allure
import pytest


@pytest.mark.medium
@pytest.mark.auth
@allure.feature('Authorization')
@allure.story('Get authorization')
class TestGetAuthorization:

    @allure.title('Get existing authorization token')
    def test_get_existing_authorization_token(self, get_authorize_token_endpoint, request):
        get_authorize_token_endpoint.get_authorize_token(request.config.token)
        get_authorize_token_endpoint.check_that_status_is_200()
        get_authorize_token_endpoint.check_auth_user_is_correct(request.config.user)

    @allure.title('Get not existing authorization token')
    def test_get_not_existing_authorization_token(self, get_authorize_token_endpoint):
        get_authorize_token_endpoint.get_authorize_token('test')
        get_authorize_token_endpoint.check_that_status_is_404()
