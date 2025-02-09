import pytest
from tests.data import POZ_DATA, NEG_DATA, MISSING_DATA, PUT_DATA, NO_ID, NEG_DATA_2

# тесты получения одного мема по id
# позитивный тест получения одного мема по id
def test_get_meme(get_one_meme_api, get_meme_id, authorization_api):
    get_one_meme_api.token = authorization_api
    get_one_meme_api.get_meme(get_meme_id)
    get_one_meme_api.check_id(get_meme_id)


# негативный тест получения одного мема по несуществующему id
def test_get_meme_wrong_id(get_one_meme_api, invalid_id, authorization_api):
    get_one_meme_api.token = authorization_api
    get_one_meme_api.get_meme(invalid_id)
    get_one_meme_api.assert_status_404()


# негативный тест получения одного мема c невалидным токеном
def test_get_meme_invalid_token(get_one_meme_api, get_meme_id,invalid_token):
    get_one_meme_api.token = invalid_token
    get_one_meme_api.get_meme(get_meme_id)
    get_one_meme_api.assert_status_401()


# тесты получения списка всех мемов
# позитивный тест получения списка всех мемов
def test_get_memes(get_all_memes_api, get_meme_id, authorization_api):
    get_all_memes_api.token = authorization_api
    get_all_memes_api.get_memes()
    get_all_memes_api.assert_status_200()


# негативный тест получения всех мемов c невалидным токеном
def test_get_memes_invalid_token(get_all_memes_api, get_meme_id, invalid_token):
    get_all_memes_api.token = invalid_token
    get_all_memes_api.get_memes()
    get_all_memes_api.assert_status_401()

# тесты добавления мема
# позитивный тест добавления нового мема
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_post_meme(post_meme_api, meme_cleanup, poz_data, authorization_api):
    post_meme_api.token = authorization_api
    post_meme_api.create_meme(poz_data)
    post_meme_api.assert_status_200()
    meme_cleanup.append(post_meme_api.json['id'])

# негативный тест добавления нового мема с неправильными типами данных
@pytest.mark.parametrize('neg_data', NEG_DATA)
def test_post_meme_incorrect_data1(post_meme_api, neg_data, authorization_api):
    post_meme_api.token = authorization_api
    post_meme_api.create_meme(neg_data)
    post_meme_api.assert_status_400()


# негативный тест добавления нового мема с недостающими данными
@pytest.mark.parametrize('missing_data', MISSING_DATA)
def test_post_meme_incorrect_data2(post_meme_api, missing_data, authorization_api):
    post_meme_api.token = authorization_api
    post_meme_api.create_meme(missing_data)
    post_meme_api.assert_status_400()


# негативный тест добавления нового мема с невалидным токеном
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_post_invalid_token(post_meme_api, poz_data, invalid_token):
    post_meme_api.token = invalid_token
    post_meme_api.create_meme(poz_data)
    post_meme_api.assert_status_401()

# тесты изменения мема по id
# позитивный тест изменения существующего мема
@pytest.mark.parametrize('put_data', PUT_DATA)
def test_put_meme(get_meme_id, put_meme_api, put_data, authorization_api):
    meme_id = get_meme_id
    put_data["id"] = meme_id
    put_meme_api.token = authorization_api
    put_meme_api.put_meme(get_meme_id, put_data)
    put_meme_api.assert_status_200()
    put_meme_api.check_put(put_data)


# негативный тест изменения мема с невалидным id
@pytest.mark.parametrize('put_data', PUT_DATA)
def test_put_meme_wrong_id(put_meme_api, put_data, invalid_id, authorization_api):
    meme_id = invalid_id
    put_data["id"] = meme_id
    put_meme_api.token = authorization_api
    put_meme_api.put_meme(invalid_id, put_data)
    put_meme_api.assert_status_404()

# позитивный тест изменения мема с теми же данными
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_put_meme_same_data(get_meme_id, put_meme_api, poz_data, authorization_api):
    meme_id = get_meme_id
    poz_data["id"] = meme_id
    put_meme_api.token = authorization_api
    put_meme_api.put_meme(get_meme_id, poz_data)
    put_meme_api.assert_status_200()
    put_meme_api.check_unchanged_data(poz_data)

# негативный тест изменения мема без переданного в теле id
@pytest.mark.parametrize('no_id', NO_ID)
def test_put_meme_no_id(get_meme_id, put_meme_api, no_id, authorization_api):
    put_meme_api.token = authorization_api
    put_meme_api.put_meme(get_meme_id, no_id)
    put_meme_api.assert_status_400()

# негативный тест изменения мема с невалидными данными
@pytest.mark.parametrize('neg_data2', NEG_DATA_2)
def test_put_meme_invalid_data(get_meme_id, put_meme_api,neg_data2, authorization_api):
    meme_id = get_meme_id
    neg_data2["id"] = meme_id
    put_meme_api.token= authorization_api
    put_meme_api.put_meme(get_meme_id, neg_data2)
    put_meme_api.assert_status_400()

# негативный тест изменения мема другого автора
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_put_another_author(put_meme_api, poz_data, new_author, authorization_api):
    meme_id = new_author
    poz_data["id"] = meme_id
    put_meme_api.token = authorization_api
    put_meme_api.put_meme(new_author, poz_data)
    put_meme_api.assert_status_403()

# тесты удаления мема по id
# позитивный тест удаления мема
def test_delete(new_meme_id, delete_meme_api, authorization_api, get_one_meme_api):
    delete_meme_api.token = authorization_api
    meme_id = new_meme_id
    delete_meme_api.delete_meme(new_meme_id)
    delete_meme_api.assert_status_200()
    get_one_meme_api.token = authorization_api
    get_one_meme_api.get_meme(meme_id)
    get_one_meme_api.assert_status_404()


# негативный тест удаленя мема по несуществующему id
def test_delete_wrong_id(delete_meme_api, invalid_id, authorization_api):
    delete_meme_api.token = authorization_api
    delete_meme_api.delete_meme(invalid_id)
    delete_meme_api.assert_status_404()

# негативный тест удаленя мема c невалидным токеном
def test_delete_invalid_token(delete_meme_api, get_meme_id, invalid_token):
    delete_meme_api.token = invalid_token
    delete_meme_api.delete_meme(get_meme_id)
    delete_meme_api.assert_status_401()
