from page.base_page import WebPage
from page.elements import WebElement
import os

class Main(WebPage):
    def __init__(self, web_driver, url=None):
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
    btn_character_hunter = WebElement(xpath="//a[@href='character/index.html?type=hunter']")



        # btn_character = WebDriverWait(web_driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'Jmain'))
        # )
        # self.btn_character = web_driver.find_element (By.CLASS_NAME, "btLink btnJs")
        # object.__setattr__(self,'btn_character', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/character.html']"))
        # object.__setattr__(self,'btn_features', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/features.html']"))
        # object.__setattr__(self, 'btn_newspage', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/newspage.html']"))
        # object.__setattr__(self,'btn_story', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/story.html']"))
        # object.__setattr__(self, 'btn_gallery', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='gallery/en/']"))
        # object.__setattr__(self, 'btn_merch', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://neteasestore.com/collections/identity-v']"))
        # object.__setattr__(self, 'btn_art_museum', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/video.html']"))
