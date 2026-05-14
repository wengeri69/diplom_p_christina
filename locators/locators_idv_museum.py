from page.base_page import WebPage
from page.elements import WebElement
import os


class Idv_museum(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_art_museum = WebElement(xpath="//a[@href='en/video.html']")
    btn_officialart = WebElement(xpath="//li[@class='navItem nav1 on']")
    btn_fanillustration = WebElement(xpath="//li[@class='navItem nav2']")
    btn_videoanimation = WebElement(xpath="//li[@class='navItem nav3']")
    btn_music = WebElement(xpath="//li[@class='navItem nav4']")
    btn_return = WebElement(xpath="//a[@class='btnReturn']")
    btn_more = WebElement(xpath="//a[@class='btnMore']")
