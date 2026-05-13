from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page6(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_gravekeeper = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953724.html']")
    btn_prisoner = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953725.html']")
    btn_entomologist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953726.html']")
    btn_painter = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210618/35290_954728.html']")
    btn_batter = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953728.html']")
