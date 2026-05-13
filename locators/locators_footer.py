from page.base_page import WebPage
import os

from page.elements import WebElement, ManyWebElements


class Adentityvgame_footer(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN") or 'https://www.identityvgame.com/'

        super().__init__(web_driver, url)

    btn_img1 = WebElement(xpath='//img[@src="https://www.identityvgame.com/pc/gw/20210609113612/img/nie_en_f87f826.png"]')
    btn_img2 = WebElement(xpath='//img[@src="https://www.identityvgame.com/pc/gw/20210609113612/img/logo_nie_d4598f1.png"]')
    btn_img3 = WebElement(xpath='//img[@src="https://www.identityvgame.com/pc/gw/20210609113612/img/copy2_d8e3aec.png"]')