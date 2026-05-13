import time
from conftest import web_browser
import allure
import pytest_check as check
from locators.locators_story import Story


@allure.feature('UI тесты')
@allure.title('Тест истории')
def test_story(web_browser):
    page = Story(web_browser)
    page.btn_backgroung.click()
    time.sleep(5)

    elements = [
        (page.btn_return, 'Return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_img_story, 'story', 'https://www.identityvgame.com/pc/gw/20210609113612/img/en/story_txt_7c18d35.png'),
        (page.btn_img_background, 'img', 'https://www.identityvgame.com/pc/gw/20210609113612/img/en/tit_4_2c93293.png'),
                ]

    for btn, txt, href in elements:
        # check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        # check.equal(btn.get_attribute('scr'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверная текст в {txt}')