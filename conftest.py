import pytest
from requests import session

from endpoints.authorize.create_authorize_token import CreateAuthorizeToken
from endpoints.authorize.get_authorize_token import GetAuthorizeToken
from endpoints.meme.get_memes import GetMemes
from endpoints.meme.get_meme import GetMeme
from endpoints.meme.create_meme import CreateMeme
from endpoints.meme.update_meme import UpdateMeme
from endpoints.meme.delete_meme import DeleteMeme


@pytest.fixture()
def create_authorize_token_endpoint():
    return CreateAuthorizeToken()


@pytest.fixture()
def get_authorize_token_endpoint():
    return GetAuthorizeToken()


@pytest.fixture()
def get_memes_endpoint():
    return GetMemes()


@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture(scope='session', autouse=True)
def create_authorize_token_for_session(request):
    auth = CreateAuthorizeToken()
    payload = {'name': 'test'}
    auth.create_authorize_token(payload)
    request.config.token = auth.token
    request.config.user = auth.user
    yield auth.token


@pytest.fixture()
def meme_id_fixture(request, create_meme_endpoint, delete_meme_endpoint):
    create_meme_endpoint.create_meme(
        payload={"text": "test", "url": "test", "tags": ["test"], "info": {"test": "test"}},
        headers={'Content-type': 'application/json', 'Authorization': request.config.token}
    )
    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(
        meme_id=create_meme_endpoint.meme_id,
        headers={'Content-type': 'application/json', 'Authorization': request.config.token})
