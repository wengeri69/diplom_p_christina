import requests


def test_survivor_page_is_available():
    url = "https://idv.163.com/en/character/index.html?type=survivors"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка выживших доступена:)")