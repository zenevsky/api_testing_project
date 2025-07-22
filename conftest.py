import pytest

from endpoints.authorize.create_authorize_token import CreateAuthorizeToken
from endpoints.authorize.get_authorize_token import GetAuthorizeToken
from endpoints.meme.get_memes import GetMemes
from endpoints.meme.get_meme import GetMeme
from endpoints.meme.create_meme import CreateMeme
from endpoints.meme.update_meme import UpdateMeme
from endpoints.meme.delete_meme import DeleteMeme

from endpoints.authorize.models.auth_object_model import AuthorizePayload
from endpoints.meme.models.meme_object_model import CreateMemePayload
from endpoints.meme.models.meme_object_model import UpdateMemePayload

from fixtures import create_authorize_token_for_session  # NOQA F401
from fixtures import meme_id_fixture  # NOQA F401


@pytest.fixture()
def create_authorize_token_endpoint():
    return CreateAuthorizeToken()


@pytest.fixture()
def get_authorize_token_endpoint():
    return GetAuthorizeToken()


@pytest.fixture(scope='session', autouse=True)
def authorize_payload():
    return AuthorizePayload()


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
def create_meme_payload():
    return CreateMemePayload()

@pytest.fixture()
def update_meme_payload():
    return UpdateMemePayload()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
