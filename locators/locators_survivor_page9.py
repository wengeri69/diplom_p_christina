from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page9(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_aeroplanist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20230718/35290_1099346.html']")
    btn_cheerleader = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20230830/35290_1107112.html']")
    btn_puppeteer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20240118/35290_1132794.html']")
    btn_fireinvestigator = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20240410/35290_1148361.html']")
    btn_farolady = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20240603/35290_1158771.html']")
