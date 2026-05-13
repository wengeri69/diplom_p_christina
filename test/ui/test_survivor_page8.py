import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_survivor_page8 import Survivor_page8


@allure.title('тесты сурвов')
def test_survivor(web_browser):
    page = Survivor_page8(web_browser)
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
    time.sleep(2)

    elements = [
        (page.btn_weepingclown, 'Weeping Clown', '//idv.163.com/en/character/survivors/20220805/35290_1035434.html'),
        (page.btn_professor, 'Professor', '//idv.163.com/en/character/survivors/20220805/35290_1035438.html'),
        (page.btn_antiquarian, 'Antiquarian', '//idv.163.com/en/character/survivors/20220805/35290_1035457.html'),
        (page.btn_composer, 'Composer', '//idv.163.com/en/character/survivors/20221130/35290_1055507.html'),
        (page.btn_journalist, 'Journalist', '//idv.163.com/en/character/survivors/20230621/35290_1094464.html'),
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