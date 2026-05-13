from page.base_page import WebPage
from page.elements import WebElement
import os


class Hunter_page5(WebPage):
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

    btn_naiad = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20210623/35292_955580.html']")
    btn_waxartist = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20211012/35292_978010.html']")
    btn_nightmare = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20211227/35292_994171.html']")
    btn_clerk = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20220805/35292_1035420.html']")
    btn_hermit = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20220815/35292_1037271.html']")

    # btn_nightwatch = WebElement(xpath="//div[@data-url = '//idv.163.com/en/character/hunters/20230621/35292_1094500.html']")
    # btn_foolsgold = WebElement(xpath="//div[@data-url='//idv.163.com/en/character/hunters/20231016/35292_1114959.html']")



