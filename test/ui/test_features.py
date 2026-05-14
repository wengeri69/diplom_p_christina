import time
import allure
from conftest import web_browser
import pytest_check as check

from locators.locators_features import Features


@allure.title('тесты музея')
def test_museum(web_browser):
    page = Features(web_browser)
    page.btn_features.click()
    page.btn_next.click()
    time.sleep(2)

    elements = [
        (page.btn_swipedslide, 'slides', 'swiper-container feaBox swiper-container-horizontal'),
        (page.btn_return, 'return', 'btnReturn'),
        (page.btn_imgs, 'imgs', 'imgs'),
        (page.btn_next, 'next', 'btnNext'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('class'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')