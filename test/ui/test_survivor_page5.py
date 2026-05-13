import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_survivor_page5 import Survivor_page5


@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page5(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    time.sleep(2)

    elements = [
        (page.btn_wildling, 'Wildling', '//idv.163.com/en/character/hunters/20210615/35290_953719.html'),
        (page.btn_barmaid, 'Barmaid', '//idv.163.com/en/character/hunters/20210615/35290_953720.html'),
        (page.btn_firstofficer, 'First Officer', '//idv.163.com/en/character/hunters/20210615/35290_953721.html'),
        (page.btn_acrobat, 'Acrobat', '//idv.163.com/en/character/hunters/20210615/35290_953722.html'),
        (page.btn_postman, 'Postman', '//idv.163.com/en/character/hunters/20210615/35290_953723.html'),
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