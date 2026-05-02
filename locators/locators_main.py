from selenium.webdriver.common.by import By
from page.base_page import WebPage
import os

from page.elements import WebElement
class Main(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("MAIN") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

        #btn_access = WebElement() тут для куки информация
        self.btn_character = WebElement(web_driver, By.CSS_SELECTOR, "a[href='en/character.html']")
        # object.__setattr__(self,'btn_features', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/features.html']"))
        # object.__setattr__(self, 'btn_newspage', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/newspage.html']"))
        # object.__setattr__(self,'btn_story', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/story.html']"))
        # object.__setattr__(self, 'btn_gallery', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='gallery/en/']"))
        # object.__setattr__(self, 'btn_merch', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='https://neteasestore.com/collections/identity-v']"))
        # object.__setattr__(self, 'btn_art_museum', WebElement(web_driver, By.CSS_SELECTOR, value="a[href='en/video.html']"))
