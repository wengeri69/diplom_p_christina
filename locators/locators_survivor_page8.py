from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page8(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_weepingclown = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20220805/35290_1035434.html']")
    btn_professor = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20220805/35290_1035438.html']")
    btn_antiquarian = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20220805/35290_1035457.html']")
    btn_composer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20221130/35290_1055507.html']")
    btn_journalist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20230621/35290_1094464.html']")
