from locators.locators_identityvgame import Adentityvgame
from conftest import web_browser
import allure
import pytest_check as check


@allure.feature('UI тесты')
@allure.title('Тест хедера')
def test_headers(web_browser):
    page = Adentityvgame(web_browser)


    elements = [
        (page.btn_logo, 'Лого', 'javascript:;'),
        (page.btn_coa, 'Coa', 'https://www.identityvgame.com/coa9/rule/en/'),
        (page.btn_redem, 'redem', 'https://www.identityvgame.com/card/en/index.html'),
        (page.btn_langbox, 'langBox', ''),
                ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверная текст в {txt}')
