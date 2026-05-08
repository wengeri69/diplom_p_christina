import time
import allure
from conftest import web_browser
from locators.locators_main import Main


@allure.title('тесты мейна')
def test_main(web_browser):
    page = Main(web_browser)
    time.sleep(2)

    page.btn_character.click()
    page.go_back()
    page.btn_features.click()
    page.go_back()
    page.btn_newspage.click()
    page.go_back()
    page.btn_story.click()
    page.go_back()
    page.btn_gallery.click()
    page.scroll_down()
    time.sleep(10)
    page.switch_to_window(0)
    page.btn_merch.click()
    time.sleep(2)
    page.switch_to_window(0)
    page.btn_art_museum.click()
    page.go_back()
    time.sleep(2)

time.sleep(3)