from page.base_page import WebPage
from page.elements import WebElement
import os


class Features(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_features = WebElement(xpath="//a[@href='en/features.html']")
    btn_swipedslide = WebElement(xpath="//div[@class='swiper-container feaBox swiper-container-horizontal']")
    btn_imgs = WebElement(xpath="//div[@class='imgs']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")
    btn_return = WebElement(xpath="//a[@class='btnReturn']")
