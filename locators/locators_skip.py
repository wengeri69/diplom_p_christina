from page.base_page import WebPage
from page.elements import WebElement
import os

class Skip(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_skip_left = WebElement(xpath="//a[@class='btnLeft']")
    btn_skip_right = WebElement(xpath="//a[@class='btnRight']")
    btn_skip_next = WebElement(xpath="//a[@class='btnNext']")
    btn_skip_prev = WebElement(xpath="//a[@class='btnPrev']")
    btn_turn_next = WebElement(xpath="//a[@class='next']")
    btn_turn_prev = WebElement(xpath="//a[@class='prev']")
    btn_return = WebElement(xpath="//a[@class='btnReturn']")