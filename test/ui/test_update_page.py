import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_update_page import Update_page


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = Update_page(web_browser)
    page.btn_newspage.click()
    page.btn_more.click()
    page.btn_update.click()
    time.sleep(2)

    elements = [
        (page.btn_return, 'Return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_news, 'News', 'https://www.identityvgame.com/en/news/official/index.html'),
        (page.btn_annonce, 'Annoncement', 'https://www.identityvgame.com/en/news/announcement/index.html'),
        (page.btn_update, 'Update', 'https://www.identityvgame.com/en/news/update/index.html'),

    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')