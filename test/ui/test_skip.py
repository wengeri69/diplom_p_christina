import time
import allure
from conftest import web_browser
from locators.locators_skip import Skip
import pytest_check as check


@allure.title('тесты скипа')
def test_skip(web_browser):
    page = Skip(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    page.btn_skip_next.click()
    time.sleep(2)

    elements = [
        (page.btn_skip_left, 'left', 'btnLeft'),
        (page.btn_skip_right, 'right', 'btnRight'),
        (page.btn_skip_next, 'next', 'btnNext'),
        (page.btn_skip_prev, 'prev', 'btnPrev'),
        (page.btn_turn_next, 'prev', 'next'),
        (page.btn_turn_prev, 'prev', 'prev'),
        (page.btn_return, 'return', 'btnReturn'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('class'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')

    # page.btn_skip_right.click()
    # page.btn_skip_right.click()
    # page.btn_skip_right.click()
    # time.sleep(2)
    # page.btn_skip_left.click()
    # page.btn_skip_left.click()
    # page.btn_skip_left.click()
    # time.sleep(2)