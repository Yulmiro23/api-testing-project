import pytest
from tests.data import POZ_DATA, NEG_DATA, MISSING_DATA, PUT_DATA, NO_ID, NEG_DATA_2

# тесты получения одного мема по id
# позитивный тест получения одного мема по id
def test_get_meme(create_get_one, setup_and_teardown, authorization_api):
    create_get_one.token = authorization_api
    create_get_one.get_meme(setup_and_teardown)
    create_get_one.check_id(setup_and_teardown)


# негативный тест получения одного мема по несуществующему id
def test_get_meme_wrong_id(create_get_one, invalid_id, authorization_api):
    create_get_one.token = authorization_api
    create_get_one.get_meme(invalid_id)
    create_get_one.check_not_found()


# негативный тест получения одного мема c невалидным токеном
def test_get_meme_invalid_token(create_get_one, setup_and_teardown,invalid_token):
    create_get_one.token = invalid_token
    create_get_one.get_meme(setup_and_teardown)
    create_get_one.check_not_unauthorized()


# тесты получения списка всех мемов
# позитивный тест получения списка всех мемов
def test_get_memes(create_get_all, setup_and_teardown, authorization_api):
    create_get_all.token = authorization_api
    create_get_all.get_memes()
    create_get_all.check_status_code()


# негативный тест получения всех мемов c невалидным токеном
def test_get_memes_invalid_token(create_get_all, setup_and_teardown, invalid_token):
    create_get_all.token = invalid_token
    create_get_all.get_memes()
    create_get_all.check_not_unauthorized()

# тесты добавления мема
# позитивный тест добавления нового мема
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_post_meme(create_post_obj, teardown, poz_data, authorization_api):
    create_post_obj.token = authorization_api
    create_post_obj.create_meme(poz_data)
    create_post_obj.check_status_code()
    teardown.append(create_post_obj.json['id'])

# негативный тест добавления нового мема с неправильными типами данных
@pytest.mark.parametrize('neg_data', NEG_DATA)
def test_post_meme_incorrect_data1(create_post_obj, neg_data, authorization_api):
    create_post_obj.token = authorization_api
    create_post_obj.create_meme(neg_data)
    create_post_obj.check_bad_request()


# негативный тест добавления нового мема с недостающими данными
@pytest.mark.parametrize('missing_data', MISSING_DATA)
def test_post_meme_incorrect_data2(create_post_obj, missing_data, authorization_api):
    create_post_obj.token = authorization_api
    create_post_obj.create_meme(missing_data)
    create_post_obj.check_bad_request()


# негативный тест добавления нового мема с невалидным токеном
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_post_invalid_token(create_post_obj, poz_data, invalid_token):
    create_post_obj.token = invalid_token
    create_post_obj.create_meme(poz_data)
    create_post_obj.check_not_unauthorized()

# тесты изменения мема по id
# позитивный тест изменения существующего мема
@pytest.mark.parametrize('put_data', PUT_DATA)
def test_put_meme(setup_and_teardown, create_put_obj, put_data, authorization_api):
    meme_id = setup_and_teardown
    put_data["id"] = meme_id
    create_put_obj.token = authorization_api
    create_put_obj.put_meme(setup_and_teardown, put_data)
    create_put_obj.check_status_code()
    create_put_obj.check_put(put_data)


# негативный тест изменения мема с невалидным id
@pytest.mark.parametrize('put_data', PUT_DATA)
def test_put_meme_wrong_id(create_put_obj, put_data, invalid_id, authorization_api):
    meme_id = invalid_id
    put_data["id"] = meme_id
    create_put_obj.token = authorization_api
    create_put_obj.put_meme(invalid_id, put_data)
    create_put_obj.check_not_found()

# позитивный тест изменения мема с теми же данными
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_put_meme_same_data(setup_and_teardown, create_put_obj, poz_data, authorization_api):
    meme_id = setup_and_teardown
    poz_data["id"] = meme_id
    create_put_obj.token = authorization_api
    create_put_obj.put_meme(setup_and_teardown, poz_data)
    create_put_obj.check_status_code()

# негативный тест изменения мема без переданного в теле id
@pytest.mark.parametrize('no_id', NO_ID)
def test_put_meme_no_id(setup_and_teardown, create_put_obj, no_id, authorization_api):
    create_put_obj.token = authorization_api
    create_put_obj.put_meme(setup_and_teardown, no_id)
    create_put_obj.check_bad_request()

# негативный тест изменения мема с невалидными данными
@pytest.mark.parametrize('neg_data2', NEG_DATA_2)
def test_put_meme_invalid_data(setup_and_teardown, create_put_obj,neg_data2, authorization_api):
    meme_id = setup_and_teardown
    neg_data2["id"] = meme_id
    create_put_obj.token= authorization_api
    create_put_obj.put_meme(setup_and_teardown, neg_data2)
    create_put_obj.check_bad_request()

# негативный тест изменения мема другого автора
@pytest.mark.parametrize('poz_data', POZ_DATA)
def test_put_another_author(create_put_obj, poz_data, new_author, authorization_api):
    meme_id = new_author
    poz_data["id"] = meme_id
    create_put_obj.token = authorization_api
    create_put_obj.put_meme(new_author, poz_data)
    create_put_obj.check_forbidden()

# тесты удаления мема по id
# позитивный тест удаления мема
def test_delete(setup, create_delete_obj, authorization_api):
    create_delete_obj.token = authorization_api
    create_delete_obj.delete_meme(setup)
    create_delete_obj.check_status_code()

# негативный тест удаленя мема по несуществующему id
def test_delete_wrong_id(create_delete_obj, invalid_id, authorization_api):
    create_delete_obj.token = authorization_api
    create_delete_obj.delete_meme(invalid_id)
    create_delete_obj.check_not_found()

# негативный тест удаленя мема c невалидным токеном
def test_delete_invalid_token(create_delete_obj, setup_and_teardown, invalid_token):
    create_delete_obj.token = invalid_token
    create_delete_obj.delete_meme(setup_and_teardown)
    create_delete_obj.check_not_unauthorized()
