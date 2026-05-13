from page.base_page import WebPage
from page.elements import WebElement
import os

class Survivor_page10(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_survivor = WebElement (xpath="//a[@href='character/index.html?type=survivors']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")

    btn_knight = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20241017/35290_1187462.html']")
    btn_meteorologist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20250114/35290_1206703.html']")
    btn_archer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20250217/35290_1212168.html']")
    btn_escapologist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20250522/35290_1236160.html']")
    btn_lanternist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/survivors/20250922/35290_1260609.html']")
