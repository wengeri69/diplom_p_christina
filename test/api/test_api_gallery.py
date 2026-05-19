import requests


def test_gallery_page_is_available():
    url = "https://www.identityvgame.com/gallery/en/"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка галереи доступена:)")