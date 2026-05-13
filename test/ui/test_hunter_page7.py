import time
import allure
from conftest import web_browser
from locators.locators_hunter_page7 import Hunter_page7
import pytest_check as check


@allure.title('тесты мейна')
def test_hunter(web_browser):
    page = Hunter_page7(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_hunter.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    time.sleep(2)


    elements = [
        (page.btn_hullabaloo, '"Hullabaloo"', '//idv.163.com/en/character/hunters/20241203/35292_1197616.html'),
        (page.btn_peddler, 'Peddler', '//idv.163.com/en/character/hunters/20250408/35292_1225544.html'),
        (page.btn_cueist, '"Cueist"', '//idv.163.com/en/character/hunters/20250812/35292_1253397.html'),
        (page.btn_queenbee, '"Queen Bee"', '//idv.163.com/en/character/hunters/20251111/35292_1270318.html'),
    ]

    for btn, txt, href in elements:
        check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
        check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
        check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
        check.equal(btn.get_attribute('data-url'), href, f'Неверная ссылка в {txt}')
        check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')

    # page.btn_next.click()
    # page.btn_next.click()
    # page.btn_next.click()
    # page.btn_next.click()
    # page.btn_next.click()
    # page.btn_next.click()
    # time.sleep(2)
    # page.btn_prev.click()
    # page.btn_prev.click()
    # page.btn_prev.click()
    # page.btn_prev.click()
    # page.btn_prev.click()
    # page.btn_prev.click()
    # time.sleep(2)

# #проверка персонажа
#     page.btn_character.click()
#     page.btn_character_hunter.click()
#     time.sleep(2)
#     page.btn_next.click()
#     page.btn_next.click()
#     page.btn_next.click()
#     page.btn_next.click()
#     page.btn_next.click()
#     time.sleep(2)
#     page.btn_nightwatch.click()
#     time.sleep(10)
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     time.sleep(2)
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     time.sleep(2)
#
#     page.btn_foolsgold.click()
#     time.sleep(10)
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     page.btn_nextturn.click()
#     time.sleep(2)
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     page.btn_prevturn.click()
#     time.sleep(2)
