import pytest

from endpoints.authorize.create_authorize_token import CreateAuthorizeToken


@pytest.fixture(scope='session', autouse=True)
def create_authorize_token_for_session(request, authorize_payload):
    auth = CreateAuthorizeToken()
    auth.create_authorize_token(authorize_payload)
    request.config.token = auth.model.token
    request.config.user = auth.model.user
    yield auth.model.token


@pytest.fixture()
def meme_id_fixture(request, create_meme_endpoint, delete_meme_endpoint, create_meme_payload):
    create_meme_endpoint.create_meme(
        payload=create_meme_payload,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    yield create_meme_endpoint.model.id
    delete_meme_endpoint.delete_meme(
        meme_id=create_meme_endpoint.model.id,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token})
