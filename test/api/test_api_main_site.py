import requests

URL = "https://idv.163.com/"


def test_site_reply():
    response = requests.get(URL)

    # проверка что сайт вернул статус 200
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("сайт доступен:)")