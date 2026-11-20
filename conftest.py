import pytest
from selenium import webdriver
import uuid
import requests

API_BASE = "https://qa-stellarburgers.education-services.ru/api"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    email = f"test_{uuid.uuid4().hex[:8]}@yandex.ru"
    password = "password123"
    name = "TestUser"
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{API_BASE}/auth/register", json=payload)
    token = response.json().get("accessToken")
    yield {"email": email, "password": password, "name": name}
    if token:
        requests.delete(f"{API_BASE}/auth/user", headers={"Authorization": token})


@pytest.fixture
def user_with_order(user):
    login_data = {"email": user["email"], "password": user["password"]}
    resp = requests.post(f"{API_BASE}/auth/login", json=login_data, verify=False)
    token = resp.json().get("accessToken")
    assert token, f"Не получен токен. Ответ API: {resp.text}"
    ingredients_resp = requests.get(f"{API_BASE}/ingredients", verify=False)
    assert ingredients_resp.status_code == 200, f"Не удалось получить ингредиенты: {ingredients_resp.text}"
    ingredients = ingredients_resp.json().get("data", [])
    assert len(ingredients) > 0, "Список ингредиентов пуст"
    ingredient_id = ingredients[0]["_id"]
    order_data = {"ingredients": [ingredient_id]}
    headers = {"Authorization": token, "Content-Type": "application/json"}
    order_resp = requests.post(f"{API_BASE}/orders", json=order_data, headers=headers, verify=False)
    assert order_resp.status_code in [200, 201, 202], \
        f"Заказ не создан! Код: {order_resp.status_code}, Ответ: {order_resp.text}"
    yield user