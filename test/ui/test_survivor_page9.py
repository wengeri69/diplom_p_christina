import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_survivor_page9 import Survivor_page9


@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page9(web_browser)
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
    time.sleep(2)

    elements = [
        (page.btn_aeroplanist, 'Aeroplanist', '//idv.163.com/en/character/survivors/20230718/35290_1099346.html'),
        (page.btn_cheerleader, 'Cheerleader', '//idv.163.com/en/character/survivors/20230830/35290_1107112.html'),
        (page.btn_puppeteer, 'Puppeteer', '//idv.163.com/en/character/survivors/20240118/35290_1132794.html'),
        (page.btn_fireinvestigator, 'Fire Investigator', '//idv.163.com/en/character/survivors/20240410/35290_1148361.html'),
        (page.btn_farolady, '"Faro Lady"', '//idv.163.com/en/character/survivors/20240603/35290_1158771.html'),
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