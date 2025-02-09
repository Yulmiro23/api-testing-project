import pytest
from endpoints.authorization import Authorization
from endpoints.post_meme import PostMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_one_meme import GetMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.put_meme import PutMeme
from faker import Faker


# Для проверки авторизации я сделала следующую логику:
# при запуске тестов проверяю - существует ли локальный файл(token.txt) с токеном
# если файл существует, считываю токен и проверяю, работает ли он
# если токен не работает, получаю новый, перезаписываю в файл новый токен
# если файла нет, создаю и записываю туда токен
@pytest.fixture(scope='session')
def authorization_api():
    authorization_session = Authorization()
    token = authorization_session.check_file()
    if token and authorization_session.check_token(token):
        return token
    else:
        new_token = authorization_session.generate_token()
        authorization_session.write_token(new_token)
        return new_token


@pytest.fixture()
def created_meme_id(authorization_api):
    data = {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    }
    meme_for_test = PostMeme()
    meme_for_test.token = authorization_api
    meme_json = meme_for_test.create_meme(data)
    meme_id = meme_json['id']
    yield meme_id
    meme_for_delete = DeleteMeme()
    meme_for_delete.token = authorization_api
    meme_for_delete.delete_meme(meme_id)


@pytest.fixture()
def get_one_meme_api():
    return GetMeme()


@pytest.fixture()
def get_all_memes_api():
    return GetAllMemes()


@pytest.fixture()
def post_meme_api():
    return PostMeme()


@pytest.fixture()
def meme_cleanup(authorization_api):
    meme_id_list = []
    yield meme_id_list
    meme_for_delete = DeleteMeme()
    meme_for_delete.token = authorization_api
    meme_for_delete.delete_meme(meme_id_list[0])


@pytest.fixture()
def new_meme_id(authorization_api):
    data = {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    }
    meme_for_test = PostMeme()
    meme_for_test.token = authorization_api
    meme_json = meme_for_test.create_meme(data)
    meme_id = meme_json['id']
    return meme_id


@pytest.fixture()
def put_meme_api():
    return PutMeme()


@pytest.fixture()
def delete_meme_api():
    return DeleteMeme()


@pytest.fixture()
def invalid_id():
    return 100000000


@pytest.fixture()
def invalid_token():
    return 'invalid_token'


@pytest.fixture()
def new_author():
    new_author = Authorization()
    faker = Faker("en_US")
    name = faker.name()
    new_author.body = {"name": name}
    new_token = new_author.generate_token()
    data = {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    }
    meme_for_test = PostMeme()
    meme_for_test.token = new_token
    meme_json = meme_for_test.create_meme(data)
    meme_id = meme_json['id']
    yield meme_id
    meme_for_delete = DeleteMeme()
    meme_for_delete.token = new_token
    meme_for_delete.delete_meme(meme_id)
