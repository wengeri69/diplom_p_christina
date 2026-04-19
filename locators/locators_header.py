from selenium.webdriver.common.by import By
from page.base_page import WebPage
import os

from page.elements import WebElement
class Header(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HEADER") or 'https://larisadolina.com/'

        super().__init__(web_driver, url)

        #btn_access = WebElement() тут для куки информация
        object.__setattr__(self,'btn_main', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/']"))
        object.__setattr__(self,'btn_news', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/news/']"))
        object.__setattr__(self, 'btn_music', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/music/']"))
        object.__setattr__(self,'btn_bio', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/bio/']"))
        object.__setattr__(self, 'btn_event', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/events/']"))
        object.__setattr__(self, 'btn_video', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://www.youtube.com/channel/UCAtbGgUbfcee81OIbFuBSqw']"))
        object.__setattr__(self, 'btn_academy', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://muscult.ru/']"))
        object.__setattr__(self, 'btn_contacts', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://larisadolina.com/contacts/']"))
