import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_gallery import Gallery


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = Gallery(web_browser)
    page.btn_gallery.click()
    page.switch_to_window(1)
    time.sleep(2)

    elements = [
        (page.btn_langBox, 'langBox', 'langBox'),
        (page.btn_logo, 'logo', 'logo'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('class'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')