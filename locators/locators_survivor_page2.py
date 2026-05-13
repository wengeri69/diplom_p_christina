from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page2(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_forward = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953690.html']")
    btn_cowboy = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953692.html']")
    btn_magician = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953693.html']")
    btn_mechanic = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953696.html']")
    btn_coordinator = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953699.html']")
