import time
import allure
import pytest_check as check
from conftest import web_browser
from locators.locators_main import Main


@allure.title('Тест мейна')
def test_main(web_browser):
    page = Main(web_browser)
    time.sleep(2)

    elements = [
        (page.btn_character, 'character', 'https://idv.163.com/en/character.html'),
        (page.btn_features, 'features', 'https://idv.163.com/en/features.html'),
        (page.btn_newspage, 'news', 'https://idv.163.com/en/newspage.html'),
        (page.btn_story, 'background', 'https://idv.163.com/en/story.html'),
        (page.btn_gallery, 'gallery', 'https://idv.163.com/gallery/en/'),
        (page.btn_merch, 'merchandise', 'https://neteasestore.com/collections/identity-v'),
        (page.btn_art_museum, 'IDV art museum', 'https://idv.163.com/en/video.html'),
        (page.btn_googleplay, 'google play', 'https://app.appsflyer.com/com.netease.idv.googleplay?pid=officialwebg&c=1'),
        (page.btn_appstore, 'app store', 'https://app.appsflyer.com/id1347780764?pid=officialwebg&c=1'),
        (page.btn_pclauncher, 'pc launcher', 'https://adl.easebar.com/d/g/idv/c/overseas?type=pc'),
                ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')