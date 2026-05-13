from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page3(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_luckyguy = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953700.html']")
    btn_priestess = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953701.html']")
    btn_themindseye = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953703.html']")
    btn_perfumer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953704.html']")
    btn_mercenary = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953705.html']")
