import time
import allure
from conftest import web_browser
from locators.locators_survivor_page1 import Survivor_page1
import pytest_check as check

@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page1(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    time.sleep(2)

    elements = [
        (page.btn_gardener, 'Gardener', '//idv.163.com/en/character/hunters/20210615/35290_953683.html'),
        (page.btn_lawyer, 'Lawyer', '//idv.163.com/en/character/hunters/20210615/35290_953684.html'),
        (page.btn_doctor, 'Doctor', '//idv.163.com/en/character/hunters/20210615/35290_953685.html'),
        (page.btn_thief, 'Thief', '//idv.163.com/en/character/hunters/20210615/35290_953688.html'),
        (page.btn_explorer, 'Explorer', '//idv.163.com/en/character/hunters/20210615/35290_953689.html'),
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