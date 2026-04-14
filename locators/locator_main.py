from conftest import web_browser
from page.base_page import WebPage
import os

from page.elements import WebElement
class Main(WebPage):
    def __unit__(self, web_driver, web_browser, url='"https://larisadolina.com/"'):
        if not url:
            url = os.getenv("MAIN") or 'https://larisadolina.com/'

        super().__unit__(web_driver, url)



