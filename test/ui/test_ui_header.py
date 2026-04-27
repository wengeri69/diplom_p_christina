import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

from conftest import web_browser
from locators.locators_header import Header


@allure.title('тесты хедера')
def test_header(web_browser):
    page = Header(web_browser)
    time.sleep(15)
    with allure.step('главная'):
        if page.btn_main.is_clickable():
            page.btn_main.click(3)
            web_browser.back()
    with allure.step('новости'):
        if page.btn_news.is_clickable():
            page. btn_news.click(3)
            web_browser.back()
    with allure.step('музыка'):
        if page.btn_music.is_clickable():
            page.btn_music.click(3)
            web_browser.back()
    with allure.step('биография'):
        if page.btn_bio.is_clickable():
            page.btn_bio.click(3)
            web_browser.back()
    with allure.step('афиша'):
        if page.btn_event.is_clickable():
            page.btn_event.click(3)
            web_browser.back()
    with allure.step('видео'):
        if page.btn_video.is_clickable():
            page.btn_video.click(3)
            web_browser.back()
    with allure.step('академия'):
        if page.btn_academy.is_clickable():
            page.btn_academy.click(3)
            web_browser.back()
    with allure.step('контакты'):
        if page.btn_contacts.is_clickable():
            page.btn_contacts.click(3)
            web_browser.back()

time.sleep(3)