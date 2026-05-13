from page.base_page import WebPage
from page.elements import WebElement
import os


class Hunter_page3(WebPage):
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

    btn_dreamwitch = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953674.html']")
    btn_evilreptilian = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953675.html']")
    btn_axeboy = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953676.html']")
    btn_bloodyqueen = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953677.html']")
    btn_guard = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/detective/20210615/35292_953678.html']")

    # btn_nightwatch = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20230621/35292_1094500.html']")
    # btn_foolsgold = WebElement(xpath="//div[@data-url='//idv.163.com/en/character/hunters/20231016/35292_1114959.html']")



