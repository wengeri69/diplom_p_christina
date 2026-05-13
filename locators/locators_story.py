from page.base_page import WebPage
import os
from page.elements import WebElement, ManyWebElements


class Story(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_backgroung = WebElement(xpath="//a[@href='en/story.html']")
    btn_return = WebElement(xpath="//a[@class='btnReturn']")

    btn_img_story = WebElement(xpath='//img[@src="https://www.identityvgame.com/pc/gw/20210609113612/img/en/story_txt_7c18d35.png"]')
    btn_img_background = WebElement(xpath='//img[@src="https://www.identityvgame.com/pc/gw/20210609113612/img/en/tit_4_2c93293.png"]')
    btn_story_href = WebElement(xpath='//div[@class="story ani"]')