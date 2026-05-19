import requests


def test_news_is_available():
    url = "https://www.identityvgame.com/en/newspage.html"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка новостей доступена:)")