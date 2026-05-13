from page.base_page import WebPage
from page.elements import WebElement
import os

class Switch(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_hunter_switch = WebElement(xpath="//a[@data-type='hunters']")
    btn_survivor_switch = WebElement(xpath="//a[@data-type='survivors']")