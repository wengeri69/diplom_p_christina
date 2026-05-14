import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_gallery_img import Gallery_img


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = Gallery_img(web_browser)
    page.btn_gallery.click()
    page.switch_to_window(1)
    time.sleep(10)
    page.scroll_down(1000)
    time.sleep(2)
    #сделать так чтобы тесты прошли а то лакаторы не видны

    elements = [
        (page.btn_img1, 'img1', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card_5ce62da.png'),
        (page.btn_img2, 'img2', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card3_66a96a4.png'),
        (page.btn_img3, 'img3', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card2_751ffca.png'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('scr'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')