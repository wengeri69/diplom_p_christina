import requests


def test_coa_page_is_available():
    url = "https://www.identityvgame.com/coa9/rule/en/"
    response = requests.get(url)
    # Проверяем статус
    assert response.status_code == 200, f"сайт недоступен, статус: {response.status_code}"
    print("вкладка coa доступена:)")