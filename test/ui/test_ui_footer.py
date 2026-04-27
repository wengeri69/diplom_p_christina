import time
import allure
from conftest import web_browser
from locators.locator_footer import Footer


@allure.title('тесты футера')
def test_footer(web_browser):
    page = Footer(web_browser)
    time.sleep(15)
    # footer_element = web_browser.find_element(id="226f095")
    # web_browser.execute_script("arguments[0].scrollIntoView(true);", footer_element)
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
    with allure.step('ютуб'):
        if page.btn_youtube.is_clickable():
            page.btn_youtube.click(3)
            web_browser.back()
    with allure.step('вк'):
        if page.btn_vk.is_clickable():
            page.btn_vk.click(3)
            web_browser.back()
    with allure.step('одноклассники'):
        if page.btn_ok.is_clickable():
            page.btn_ok.click(3)
            web_browser.back()
    with allure.step('телеграм'):
        if page.btn_tg.is_clickable():
            page.btn_tg.click(3)
            web_browser.back()
    with allure.step('телефон'):
        if page.btn_phone.is_clickable():
            page.btn_phone.click(3)
            web_browser.back()

time.sleep(3)