import requests


def test_more_museum_page_is_available():
    url = "https://www.identityvgame.com/en/stzx/index.html?part=1"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка более обширный музей артов доступена:)")