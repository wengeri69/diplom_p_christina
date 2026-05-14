import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_idv_museum import Idv_museum


@allure.title('тесты музея')
def test_museum(web_browser):
    page = Idv_museum(web_browser)
    page.btn_art_museum.click()
    time.sleep(2)


    elements = [
        (page.btn_officialart, 'Official Art', 'navItem nav1 on'),
        (page.btn_fanillustration, 'Fan Illustration', 'navItem nav2'),
        (page.btn_videoanimation, 'Video Animation', 'navItem nav3'),
        (page.btn_music, 'Music', 'navItem nav4'),
        (page.btn_return, 'Return', 'btnReturn'),
        (page.btn_more, 'More', 'btnMore'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('class'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')
