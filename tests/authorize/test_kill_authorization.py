import allure
import pytest

from endpoints.authorize.models.auth_object_model import AuthorizePayload


@pytest.mark.medium
@pytest.mark.auth
@allure.feature('Authorization')
@allure.story('Kill authorization')
class TestKillAuthorization:

    @allure.title('Kill existing authorization token')
    def test_kill_existing_authorization_token(self, create_authorize_token_endpoint, get_authorize_token_endpoint,
                                               kill_authorize_token_endpoint):
        create_authorize_token_endpoint.create_authorize_token(AuthorizePayload())
        token = create_authorize_token_endpoint.model.token
        kill_authorize_token_endpoint.kill_authorize_token(token)
        get_authorize_token_endpoint.get_authorize_token_and_check_that_status_is_404(token)

    @allure.title('Kill not existing authorization token')
    def test_kill_not_existing_authorization_token(self, get_authorize_token_endpoint, kill_authorize_token_endpoint):
        kill_authorize_token_endpoint.kill_authorize_token('test')
        kill_authorize_token_endpoint.check_that_status_is_404()
