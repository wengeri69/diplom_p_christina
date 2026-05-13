from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page4(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_femaledancer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953706.html']")
    btn_seer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953710.html']")
    btn_embalmer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953712.html']")
    btn_prospector = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953714.html']")
    btn_enchantress = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953717.html']")
