import requests


def test_character_page_is_available():
    url = "https://idv.163.com/en/character.html"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка выбора персонажей доступена:)")