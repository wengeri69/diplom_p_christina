import driver
from selenium.webdriver.common.by import By

from page.base_page import WebPage
import os

from page.elements import WebElement
class Header(WebPage):
    def __init__(self, web_driver, url='"https://larisadolina.com/"'):
        if not url:
            url = os.getenv("HEADER") or 'https://larisadolina.com/'

        super().__init__(web_driver, url)

        #btn_access = WebElement() тут для куки информация
        btn_main = driver.find_element(By.CSS_SELECTOR, "a[href='https://larisadolina.com/']")
        btn_news = driver.find_element(By.CSS_SELECTOR, "a[href='https://larisadolina.com/news/']")
        btn_music = driver.find_element(By.CSS_SELECTOR, "a[href='https://larisadolina.com/music/']")
        btn_bio = driver.find_element(By.CSS_SELECTOR, "a[href='https://larisadolina.com/bio/']")
        # btn_main = WebElement(href='href="https://larisadolina.com/"')
        # btn_news = WebElement(href='"https://larisadolina.com/news/"')
        # btn_music = WebElement(href='href="https://larisadolina.com/music/"')
        # btn_bio = WebElement(href='href="https://larisadolina.com/bio/"')