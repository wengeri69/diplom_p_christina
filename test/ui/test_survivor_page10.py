import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_survivor_page10 import Survivor_page10


@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page10(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    time.sleep(2)

    elements = [
        (page.btn_knight, '"Knight"', '//idv.163.com/en/character/survivors/20241017/35290_1187462.html'),
        (page.btn_meteorologist, 'Meteorologist', '//idv.163.com/en/character/survivors/20250114/35290_1206703.html'),
        (page.btn_archer, 'Archer', '//idv.163.com/en/character/survivors/20250217/35290_1212168.html'),
        (page.btn_escapologist, '"Escapologist"', '//idv.163.com/en/character/survivors/20250522/35290_1236160.html'),
        (page.btn_lanternist, 'Lanternist', '//idv.163.com/en/character/survivors/20250922/35290_1260609.html'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('data-url'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')

    # page.btn_gardener.click()
    # time.sleep(2)
    # page.btn_nextturn.click()
    # page.btn_nextturn.click()
    # page.btn_nextturn.click()
    # time.sleep(2)
    # page.btn_prevturn.click()
    # page.btn_prevturn.click()
    # page.btn_prevturn.click()
    # time.sleep(2)
    #
    # page.btn_doctor.click()
    # time.sleep(2)
    # page.btn_nextturn.click()
    # page.btn_nextturn.click()
    # page.btn_nextturn.click()
    # time.sleep(2)
    # page.btn_prevturn.click()
    # page.btn_prevturn.click()
    # page.btn_prevturn.click()
    # time.sleep(2)