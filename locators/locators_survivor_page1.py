from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page1(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_gardener = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953683.html']")
    btn_lawyer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953684.html']")
    btn_doctor = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953685.html']")
    btn_thief = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953688.html']")
    btn_explorer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953689.html']")
