from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page11(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_matador = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20260123/35290_1283385.html']")
