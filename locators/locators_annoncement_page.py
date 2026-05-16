from page.base_page import WebPage
from page.elements import WebElement
import os


class Announce_page(WebPage):
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

    btn_announce1 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260512/35288_1300004.html']")
    btn_announce2 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260416/35288_1296458.html']")
    btn_announce3 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260409/35288_1295335.html']")
    btn_announce4 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260409/35288_1295334.html']")
    btn_announce5 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260326/35288_1293094.html']")
    btn_announce6 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260326/35288_1293061.html']")
    btn_announce7 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260312/35288_1290790.html']")
    btn_announce8 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260305/35288_1289644.html']")
    btn_announce9 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260227/35288_1288559.html']")
    btn_announce10 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260205/35288_1285646.html']")
    btn_announce11 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260129/35288_1284409.html']")
    btn_announce12 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260123/35288_1283378.html']")
    btn_announce13 = WebElement(xpath="//a[@href='https://www.identityvgame.com/en/news/announcement/20260116/35288_1282125.html']")
    btn_page2 = WebElement(xpath="//a[@href='https://idv.163.com/en/news/announcement/index_2.html']")
    btn_page3 = WebElement(xpath="//a[@href='https://idv.163.com/en/news/announcement/index_3.html']")
    btn_page4 = WebElement(xpath="//a[@href='https://idv.163.com/en/news/announcement/index_4.html']")
    btn_page5 = WebElement(xpath="//a[@href='https://idv.163.com/en/news/announcement/index_5.html']")