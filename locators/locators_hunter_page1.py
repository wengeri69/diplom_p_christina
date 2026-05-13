from page.base_page import WebPage
from page.elements import WebElement
import os


class Hunter_page1(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement(xpath="//a[@href='en/character.html']")
    btn_hunter = WebElement(xpath="//a[@href='character/index.html?type=hunter']")

    btn_next = WebElement(xpath="//a[@class='btnNext']")
    btn_prev = WebElement(xpath="//a[@class='btnPrev']")
    btn_nextturn = WebElement(xpath="//a[@class='next']")
    btn_prevturn = WebElement(xpath="//a[@class='prev']")

    btn_hellember = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953640.html']")
    btn_theripper = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953665.html']")
    btn_smileyface = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953664.html']")
    btn_gamekeeper = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953666.html']")
    btn_thefeaster = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953667.html']")

    # btn_nightwatch = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20230621/35292_1094500.html']")
    # btn_foolsgold = WebElement(xpath="//div[@data-url='//idv.163.com/en/character/hunters/20231016/35292_1114959.html']")



