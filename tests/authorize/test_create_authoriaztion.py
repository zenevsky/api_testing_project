import allure
import pytest

from endpoints.authorize.models.auth_object_model import AuthorizePayload
from helpers.create_authorize_token_test_data import NEGATIVE_DATA


@pytest.mark.auth
@allure.feature('Authorization')
@allure.story('Create authorization')
class TestCreateAuthorization:

    @pytest.mark.critical
    @allure.title('Create authorization token with valid name')
    def test_create_auth_with_valid(self, create_authorize_token_endpoint, authorize_payload):
        create_authorize_token_endpoint.create_authorize_token(payload=AuthorizePayload())
        create_authorize_token_endpoint.check_that_status_is_200()
        create_authorize_token_endpoint.check_auth_user_is_correct(authorize_payload.name)


    @pytest.mark.parametrize(
        'data', NEGATIVE_DATA
    )
    @pytest.mark.medium
    @allure.title('Create authorization token with invalid name')
    def test_create_auth_with_invalid_name(self, create_authorize_token_endpoint, data):
        payload = data if data == {} else AuthorizePayload(**data)
        create_authorize_token_endpoint.create_authorize_token(payload=payload)
        create_authorize_token_endpoint.check_that_status_is_400()
