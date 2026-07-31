import pytest


@pytest.mark.positive
def test_authentication(api):
    """Позитивный: успешная авторизация."""
    response = api.create_project("Проверка авторизации")
    assert response.status_code == 201


@pytest.mark.positive
def test_add_new_project(api):
    response = api.create_project("Учеба 2026")
    assert response.status_code == 201
    assert "id" in response.json()


@pytest.mark.positive
def test_get_one_project(api):
    api.create_project("Учеба 2026")
    response = api.get_project(project_id=api.project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Учеба 2026"


@pytest.mark.positive
def test_update_one_project(api):
    api.create_project("Учеба 2026")
    response = api.update_project("Скоро диплом", project_id=api.project_id)
    assert response.status_code == 200
    assert "id" in response.json()


@pytest.mark.negative
def test_add_new_project_empty_title(api):
    response = api.create_project("")
    assert response.status_code == 400


@pytest.mark.negative
def test_non_existing_project(api):
    response = api.get_project(project_id="несуществующий-id")
    assert response.status_code == 404


@pytest.mark.negative
def test_update_nonexistent_project(api):
    response = api.update_project("Глобус", project_id="несуществующий-id")
    assert response.status_code == 404
