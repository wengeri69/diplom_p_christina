import time

import allure

from conftest import web_browser
from locators.locators_header import Header


@allure.title('4534534')
def test_header_chat(web_browser):
    page = Header(web_browser)
    #кликабельность
    #лучше найти сайт другой где есть куки и потом проверить как делали в белбет
    #page.btn_access.click(3) тут проверка

    with allure.step('43234'):
        if page.btn_main.is_clickable():
            page.btn_main.click(3)

    # data = [] если есть дата(данные)
    #
    # for btn, text in data:
    #     with allure.step(f'проверка кликабельности {text}'):
    #         assert btn.is_clickable() #f'некликабельна {text}'