import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_annoncement_page import Announce_page


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = Announce_page(web_browser)
    page.btn_newspage.click()
    page.btn_more.click()
    page.scroll_down(600)
    time.sleep(2)

    elements = [
        (page.btn_return, 'Return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_news, 'News', 'https://www.identityvgame.com/en/news/official/index.html'),
        (page.btn_annonce, 'Annoncement', 'https://www.identityvgame.com/en/news/announcement/index.html'),
        (page.btn_update, 'Update', 'https://www.identityvgame.com/en/news/update/index.html'),

        (page.btn_announce1, 'Maintenance Update on May 8', 'https://www.identityvgame.com/en/news/announcement/20260512/35288_1300004.html'),
        (page.btn_announce2, 'Maintenance Update on April 16', 'https://www.identityvgame.com/en/news/announcement/20260416/35288_1296458.html'),
        (page.btn_announce3, 'Test Server Maintenance Update on April 9', 'https://www.identityvgame.com/en/news/announcement/20260409/35288_1295335.html'),
        (page.btn_announce4, 'Maintenance Update on April 9', 'https://www.identityvgame.com/en/news/announcement/20260409/35288_1295334.html'),
        (page.btn_announce5, 'Limited-Time 1V4 & 2V8 Entertainment Mode Submission Contest', 'https://www.identityvgame.com/en/news/announcement/20260326/35288_1293094.html'),
        (page.btn_announce6, 'Maintenance Update on March 26', 'https://www.identityvgame.com/en/news/announcement/20260326/35288_1293061.html'),
        (page.btn_announce7, 'Maintenance Update on March 12', 'https://www.identityvgame.com/en/news/announcement/20260312/35288_1290790.html'),
        (page.btn_announce8, 'Maintenance Update on March 5', 'https://www.identityvgame.com/en/news/announcement/20260305/35288_1289644.html'),
        (page.btn_announce9, 'Maintenance Update on February 27','https://www.identityvgame.com/en/news/announcement/20260227/35288_1288559.html'),
        (page.btn_announce10, 'Maintenance Update on February 5','https://www.identityvgame.com/en/news/announcement/20260205/35288_1285646.html'),
        (page.btn_announce11, 'Maintenance Update on January 29','https://www.identityvgame.com/en/news/announcement/20260129/35288_1284409.html'),
        (page.btn_announce12, 'Test Server Maintenance Update on January 23','https://www.identityvgame.com/en/news/announcement/20260123/35288_1283378.html'),
        (page.btn_announce13, 'Maintenance Update on December January 15','https://www.identityvgame.com/en/news/announcement/20260116/35288_1282125.html'),

        (page.btn_page2, '2','https://idv.163.com/en/news/announcement/index_2.html'),
        (page.btn_page3, '3','https://idv.163.com/en/news/announcement/index_3.html'),
        (page.btn_page4, '4','https://idv.163.com/en/news/announcement/index_4.html'),
        (page.btn_page5, '5','https://idv.163.com/en/news/announcement/index_5.html'),

    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')