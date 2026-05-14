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
    btn_twitter = WebElement(xpath="////a[@href='https://twitter.com/GameIdentityV']")
    btn_more = WebElement(xpath="////a[@class='btnMore']")
    # btn_news = WebElement(xpath="////li[@class='on']")
    # btn_announcement = WebElement(xpath="////li[@class='on']")
    # btn_update = WebElement(xpath="////li[@class='on']")
    btn_firstnews = WebElement(xpath="////a[@href='https://www.identityvgame.com/en/news/official/20260212/35287_1286869.html']")
    btn_secondnews = WebElement(xpath="////a[@href='https://www.identityvgame.com/en/news/official/20241227/35287_1203026.html']")
    btn_thridnews = WebElement(xpath="////a[@href='https://www.identityvgame.com/en/news/official/20240618/35287_1161719.html']")