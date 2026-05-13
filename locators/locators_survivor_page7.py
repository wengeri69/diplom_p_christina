from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page7(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_toymerchant = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210615/35290_953727.html']")
    btn_patient = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20211012/35290_978000.html']")
    btn_psychologist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20211012/35290_978006.html']")
    btn_novelist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20211227/35290_994160.html']")
    btn_littlegirl = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20211227/35290_994166.html']")
