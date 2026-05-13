import time
import allure
from conftest import web_browser
from locators.locators_character import Character
import pytest_check as check

@allure.title('тесты сурвов')
def test_character(web_browser):
    page = Character(web_browser)
    time.sleep(2)
    page.btn_character.click()

    elements = [
        (page.btn_survivor, 'survivor', 'https://idv.163.com/en/character/index.html?type=survivors'),
        (page.btn_hunter, 'hunter', 'https://idv.163.com/en/character/index.html?type=hunter'),
        (page.btn_return, 'return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_detective, 'detective', 'javascript:;'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')