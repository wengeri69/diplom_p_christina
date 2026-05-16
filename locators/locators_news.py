from page.base_page import WebPage
from page.elements import WebElement
import os


class News(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_newspage = WebElement(xpath="//a[@href='en/newspage.html']")

    btn_swiper = WebElement(xpath="//div[@class='swiper-wrapper']")
    btn_more = WebElement(xpath="//a[@class='btnMore']")
    btn_return = WebElement(xpath="//a[@class='btnReturn']")