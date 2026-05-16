from page.base_page import WebPage
from page.elements import WebElement
import os


class Update_page(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_newspage = WebElement(xpath="//a[@href='en/newspage.html']")
    btn_more = WebElement(xpath="//a[@class='btnMore']")
    btn_return = WebElement(xpath="//a[@href='https://www.identityvgame.com/index.html?re=1']")
    btn_news = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/index.html']")
    btn_annonce = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/index.html']")
    btn_update = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/update/index.html']")
