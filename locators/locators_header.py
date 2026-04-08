from page.base_page import WebPage
import os

from page.elements import WebElement
class Header(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("HEADER") or 'https://larisadolina.com/'

        super().__init__(web_driver, url)

        #btn_access = WebElement() тут для куки информация
        btn_main = WebElement(href='href="https://larisadolina.com/"') #почитать о том как эти ссылки делать правильно
        btn_news = WebElement(href='"https://larisadolina.com/news/"')
        btn_music = WebElement(href='href="https://larisadolina.com/music/"')
        btn_bio = WebElement(href='href="https://larisadolina.com/bio/"')