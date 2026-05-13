import time
import allure
from conftest import web_browser
from locators.locators_hunter_page6 import Hunter_page6
import pytest_check as check


@allure.title('тесты мейна')
def test_hunter(web_browser):
    page = Hunter_page6(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_hunter.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    page.btn_next.click()
    time.sleep(2)


    elements = [
        (page.btn_nightwatch, 'Night Watch', '//idv.163.com/en/character/hunters/20230621/35292_1094500.html'),
        (page.btn_operasinger, 'Opera Singer', '//idv.163.com/en/character/hunters/20230621/35292_1094562.html'),
        (page.btn_foolsgold, ''' “Fool's Gold" ''', '//idv.163.com/en/character/hunters/20231016/35292_1114959.html'),
        (page.btn_theshadow, 'The shadow', '//idv.163.com/en/character/hunters/20240301/35292_1140765.html'),
        (page.btn_goatman, '"Goatman"', '//idv.163.com/en/character/hunters/20240806/35292_1172208.html'),
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
