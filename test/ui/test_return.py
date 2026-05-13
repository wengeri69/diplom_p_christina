import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_return import Return


@allure.title('тесты возвращения на главную страницу')
def test_return(web_browser):
    page = Return(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    time.sleep(2)

    elements = [
        (page.btn_return, 'return', 'https://www.identityvgame.com/index.html?re=1'),
        (page.btn_logo, 'logo', 'https://www.identityvgame.com/index.html?re=1'),
                ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')

#старый тест
# @allure.title('тесты возвращения на главную страницу')
# def test_return(web_browser):
#     page = Return(web_browser)
#     time.sleep(2)
    # # кнопка ретурн
    # page.btn_character.click()
    # page.btn_survivor.click()
    # time.sleep(2)
    # page.btn_return.click()
    # time.sleep(2)
    # # кнопка логотипа
    # page.btn_character.click()
    # page.btn_survivor.click()
    # time.sleep(2)
    # page.btn_logo.click()
    # time.sleep(2)
    # # кнопка ретурн в части где выбор хант или сурв
    # page.btn_character.click()
    # time.sleep(2)
    # page.btn_return.click()
    # time.sleep(2)