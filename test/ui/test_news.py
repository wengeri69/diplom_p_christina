import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_news import News


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = News(web_browser)
    page.btn_newspage.click()
    time.sleep(2)
    # page.btn_announcement.click()
    # time.sleep(2)
    # page.btn_update.click()
    # time.sleep(2)

    #сделать так чтобы тесты прошли а то лакаторы не видны

    elements = [
        (page.btn_swiper, 'swiper', 'swiper-wrapper'),
        (page.btn_twitter, 'x', 'https://twitter.com/GameIdentityV'),
        (page.btn_more, '+more', 'btnMore'),
        # (page.btn_news, 'News', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card2_751ffca.png'),
        # (page.btn_announcement, 'Announcement', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card2_751ffca.png'),
        # (page.btn_update, 'Update', 'https://idv.res.netease.com/pc/zt/20221221175120/img/en/card2_751ffca.png'),
        (page.btn_firstnews, 'news1', 'https://www.identityvgame.com/en/news/official/20260212/35287_1286869.html'),
        (page.btn_secondnews, 'news2', 'https://www.identityvgame.com/en/news/official/20241227/35287_1203026.html'),
        (page.btn_thridnews, 'news3', 'https://www.identityvgame.com/en/news/official/20240618/35287_1161719.html'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('class, href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')