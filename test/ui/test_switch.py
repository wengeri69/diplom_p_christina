import time
import allure
from conftest import web_browser
from locators.locators_switch import Switch


@allure.title('тесты сурвов')
def test_switch(web_browser):
    page = Switch(web_browser)
    time.sleep(2)
    page.btn_character.click()
    page.btn_survivor.click()
    time.sleep(2)

    page.btn_hunter_switch.click()
    time.sleep(2)
    page.btn_survivor_switch.click()
    time.sleep(2)