from page.base_page import WebPage
from page.elements import WebElement
import os


class News_page(WebPage):
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

    btn_news1 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20260212/35287_1286869.html']")
    btn_news2 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20241227/35287_1203026.html']")
    btn_news3 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20240618/35287_1161719.html']")
    btn_news4 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20220606/35287_1022484.html']")
    btn_news5 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20220511/35287_1017245.html']")
    btn_news6 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20220317/35287_1007840.html']")
    btn_news7 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20220303/35287_1005213.html']")
    btn_news8 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/official/20220126/35287_1000055.html']")