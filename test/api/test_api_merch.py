import requests


def test_merch_page_is_available():
    url = "https://neteasestore.com/collections/identity-v"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка мерча доступена:)")