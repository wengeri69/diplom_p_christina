from page.base_page import WebPage
import os
from page.elements import WebElement, ManyWebElements


class Adentityvgame(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://www.identityvgame.com/'

        super().__init__(web_driver, url)

    btn_logo = WebElement(xpath='//a[@class="logo"]')
    btn_coa = WebElement(xpath='//a[@class="btnCoa"]')
    btn_redem = WebElement(xpath='//a[@class="btnredem"]')
    btn_langbox = WebElement(xpath='//div[@class="langBox"]')
