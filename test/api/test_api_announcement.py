import requests


def test_announcement_page_is_available():
    url = "https://www.identityvgame.com/en/news/announcement/index.html"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка новостей-анонсов доступена:)")