import time
import allure
from conftest import web_browser
import pytest_check as check

from locators.locators_news_page import News_page


@allure.title('тесты музея')
def test_gallery_header(web_browser):
    page = News_page(web_browser)
    page.btn_newspage.click()
    page.btn_more.click()
    page.btn_news.click()
    page.scroll_down(600)
    time.sleep(2)

    elements = [
        (page.btn_return, 'Return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_news, 'News', 'https://www.identityvgame.com/en/news/official/index.html'),
        (page.btn_annonce, 'Annoncement', 'https://www.identityvgame.com/en/news/announcement/index.html'),
        (page.btn_update, 'Update', 'https://www.identityvgame.com/en/news/update/index.html'),
        (page.btn_news1, 'Maintenance Update on February 12', 'https://www.identityvgame.com/en/news/official/20260212/35287_1286869.html'),
        (page.btn_news2, 'The 1st "Scribbled Ideas" Map Contest has officially begun!', 'https://www.identityvgame.com/en/news/official/20241227/35287_1203026.html'),
        (page.btn_news3, '第五人格海外华人交流社群正式启动', 'https://www.identityvgame.com/en/news/official/20240618/35287_1161719.html'),
        (page.btn_news4, 'Identity V - Brand New Novel Series', 'https://www.identityvgame.com/en/news/official/20220606/35287_1022484.html'),
        (page.btn_news5, 'Identity V - Brand New Novel Series', 'https://www.identityvgame.com/en/news/official/20220511/35287_1017245.html'),
        (page.btn_news6, 'IOS-Android data migration notice', 'https://www.identityvgame.com/en/news/official/20220317/35287_1007840.html'),
        (page.btn_news7, 'Identity V - Brand New Novel Series', 'https://www.identityvgame.com/en/news/official/20220303/35287_1005213.html'),
        (page.btn_news8, 'Identity V - Brand New Novel Series', 'https://www.identityvgame.com/en/news/official/20220126/35287_1000055.html'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')