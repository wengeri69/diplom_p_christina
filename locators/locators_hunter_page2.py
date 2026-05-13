from page.base_page import WebPage
from page.elements import WebElement
import os


class Hunter_page2(WebPage):
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

    btn_geisha = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953669.html']")
    btn_soulweaver = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953670.html']")
    btn_wuchang = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953671.html']")
    btn_photographer = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953672.html']")
    btn_madeyes = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953673.html']")

    # btn_nightwatch = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20230621/35292_1094500.html']")
    # btn_foolsgold = WebElement(xpath="//div[@data-url='//idv.163.com/en/character/hunters/20231016/35292_1114959.html']")



