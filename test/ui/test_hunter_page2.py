import time
import allure
from conftest import web_browser
from locators.locators_hunter_page2 import Hunter_page2
import pytest_check as check


@allure.title('тесты мейна')
def test_hunter(web_browser):
    page = Hunter_page2(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_hunter.click()
    page.btn_next.click()
    time.sleep(2)


    elements = [
        (page.btn_geisha, 'Geisha', '//idv.163.com/en/character/detective/20210615/35292_953669.html'),
        (page.btn_soulweaver, 'Soul Weaver', '//idv.163.com/en/character/detective/20210615/35292_953670.html'),
        (page.btn_wuchang, 'Wu Chang', '//idv.163.com/en/character/detective/20210615/35292_953671.html'),
        (page.btn_photographer, 'Photographer', '//idv.163.com/en/character/detective/20210615/35292_953672.html'),
        (page.btn_madeyes, 'Mad Eyes', '//idv.163.com/en/character/detective/20210615/35292_953673.html'),
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
