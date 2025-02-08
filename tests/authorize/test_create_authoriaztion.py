import allure
import pytest


@pytest.mark.critical
@allure.feature('Authorization')
@allure.story('Create authorization')
@allure.title('Create authorization token with valid name')
def test_create_auth_with_valid(create_authorize_token_endpoint):
    data = {'name': 'test test'}
    create_authorize_token_endpoint.create_authorize_token(payload=data)
    create_authorize_token_endpoint.check_that_status_is_200()
    create_authorize_token_endpoint.check_auth_user_is_correct(data['name'])


@pytest.mark.parametrize(
    'data', [
        {'name': 123},
        {'name': None},
        {'name': {"test": "test"}},
        {'name': True},
        {'name': [123, "test", False]},
        {}
    ]
)
@pytest.mark.medium
@allure.feature('Authorization')
@allure.story('Create authorization')
@allure.title('Create authorization token with invalid name')
def test_create_auth_with_invalid_name(create_authorize_token_endpoint, data):
    create_authorize_token_endpoint.create_authorize_token(payload=data)
    create_authorize_token_endpoint.check_that_status_is_400()
