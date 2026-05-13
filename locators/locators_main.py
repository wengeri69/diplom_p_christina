from page.base_page import WebPage
from page.elements import WebElement
import os

class Main(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_character = WebElement (xpath="//a[@href='en/character.html']")
    btn_features = WebElement(xpath="//a[@href='en/features.html']")
    btn_newspage = WebElement(xpath="//a[@href='en/newspage.html']")
    btn_story = WebElement(xpath="//a[@href='en/story.html']")
    btn_gallery = WebElement(xpath="//a[@href='gallery/en/']")
    btn_merch = WebElement(xpath="//a[@href='https://neteasestore.com/collections/identity-v']")
    btn_art_museum = WebElement(xpath="//a[@href='en/video.html']")
    btn_downbox = WebElement(xpath="//div[@class='downbox downboxen']")

    btn_googleplay = WebElement(xpath="//a[@href='https://app.appsflyer.com/com.netease.idv.googleplay?pid=officialwebg&c=1']")
    btn_appstore = WebElement(xpath="//a[@href='https://app.appsflyer.com/id1347780764?pid=officialwebg&c=1']")
    btn_pclauncher = WebElement(xpath="//a[@href='https://adl.easebar.com/d/g/idv/c/overseas?type=pc' and @class='btnApp']")
