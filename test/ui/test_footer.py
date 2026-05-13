from conftest import web_browser
import allure
import pytest_check as check
from locators.locators_footer import Adentityvgame_footer


@allure.feature('UI тесты')
@allure.title('Тест футера')
def test_footer(web_browser):
    page = Adentityvgame_footer(web_browser)


    elements = [
        (page.btn_img1, 'img1', 'https://www.identityvgame.com/pc/gw/20210609113612/img/nie_en_f87f826.png'),
        (page.btn_img2, 'logo', 'https://www.identityvgame.com/pc/gw/20210609113612/img/logo_nie_d4598f1.png'),
        (page.btn_img3, 'img3', 'https://www.identityvgame.com/pc/gw/20210609113612/img/copy2_d8e3aec.png'),
                ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('src'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')