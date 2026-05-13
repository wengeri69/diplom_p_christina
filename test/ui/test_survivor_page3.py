import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_survivor_page3 import Survivor_page3


@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page3(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    page.btn_next.click()
    page.btn_next.click()
    time.sleep(2)

    elements = [
        (page.btn_luckyguy, 'Lucky Guy', '//idv.163.com/en/character/hunters/20210615/35290_953700.html'),
        (page.btn_priestess, 'Priestess', '//idv.163.com/en/character/hunters/20210615/35290_953701.html'),
        (page.btn_themindseye, "The Mind's Eye", '//idv.163.com/en/character/hunters/20210615/35290_953703.html'),
        (page.btn_perfumer, 'Perfumer', '//idv.163.com/en/character/hunters/20210615/35290_953704.html'),
        (page.btn_mercenary, 'Mercenary', '//idv.163.com/en/character/hunters/20210615/35290_953705.html'),
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