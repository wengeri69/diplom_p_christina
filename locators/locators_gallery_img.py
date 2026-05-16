from page.base_page import WebPage
from page.elements import WebElement
import os


class Gallery_img(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_gallery = WebElement(xpath="//a[@href='gallery/en/']")

    btn_img1 = WebElement(xpath="//img[@src='https://idv.res.netease.com/pc/zt/20221221175120/img/en/card_5ce62da.png']")
    btn_img2 = WebElement(xpath="//img[@src='https://idv.res.netease.com/pc/zt/20221221175120/img/en/card3_66a96a4.png']")
    btn_img3 = WebElement(xpath="//img[@src='https://idv.res.netease.com/pc/zt/20221221175120/img/en/card2_751ffca.png']")
