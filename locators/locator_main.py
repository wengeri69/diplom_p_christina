from page.base_page import WebPage
import os

from page.elements import WebElement
class Main(WebPage):
    def __unit__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://larisadolina.com/'

        super().__unit__(web_driver, url)

        btn_access = WebElement(xpath='')
        btn_main = WebElement(id='')
        btn_chat = WebElement(id='')

