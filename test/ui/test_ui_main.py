import time
from telnetlib import EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import web_browser
from locators.locators_main import Main


@allure.title('тесты мейна')
def test_main(web_browser):
    page = Main(web_browser)
    time.sleep(5)

    with allure.step('персонажи'):
        WebDriverWait(web_browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='en/character.html']"))
        )
        assert page.self.btn_character is not None, "Кнопка 'персонажи' не найдена"
        page.self.btn_character.click()
        # web_browser.back()





    # with allure.step('особенности'):
    #     if page.btn_features.is_clickable():
    #         page.btn_features.click(3)
    #         web_browser.back()
    # with allure.step('новости'):
    #     if page.btn_newspage.is_clickable():
    #         page.btn_newspage.click(3)
    #         web_browser.back()
    # with allure.step('история'):
    #     if page.btn_story.is_clickable():
    #         page.btn_story.click(3)
    #         web_browser.back()
    # with allure.step('галерея'):
    #     if page.btn_gallery.is_clickable():
    #         page.btn_gallery.click(3)
    #         web_browser.back()
    # with allure.step('магазин мерча'):
    #     if page.btn_merch.is_clickable():
    #         page.btn_merch.click(3)
    #         web_browser.back()
    # with allure.step('музей артов(исскуства)'):
    #     if page.btn_art_museum.is_clickable():
    #         page.btn_art_museum.click(3)
    #         web_browser.back()


time.sleep(3)