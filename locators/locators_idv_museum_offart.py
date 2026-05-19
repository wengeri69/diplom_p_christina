from page.base_page import WebPage
from page.elements import WebElement
import os


class Idv_museum_offart(WebPage):
    def __init__(self, web_driver, url=None):
        if not url:
            url = os.getenv("HUNTER") or 'https://idv.163.com/'

        super().__init__(web_driver, url)

    btn_art_museum = WebElement(xpath="//a[@href='en/video.html']")
    btn_more = WebElement(xpath="//a[@class='btnMore']")

    btn_officialart = WebElement(xpath="//li[@class='navItem nav1 on']")
    btn_fanillustration = WebElement(xpath="//li[@class='navItem nav2']")
    btn_videoanimation = WebElement(xpath="//li[@class='navItem nav3']")
    btn_music = WebElement(xpath="//li[@class='navItem nav4']")
    # btn_scroll = WebElement(xpath="//div[contains(@class, 'artBox')]")

    # btn_artboxscroll = WebElement(xpath="//div[@class='nicescroll-rails' and @id='ascrail2000']") два локатора скрола внутри сайта
    btn_scroll = WebElement(xpath="//div[@style='position: relative; top: 651px; float: right; width: 7px; height: 483px; background-color: rgb(205, 68, 56); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; background-clip: padding-box; border-radius: 10px;']")

    btn_return = WebElement(xpath="//a[@class='btnReturn']")
    btn_logo = WebElement(xpath="//a[@class='logo']")

    btn_img1 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/2489f8d015797103167e4ebed5f4c2bd.jpg']")
    btn_img2 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/ac03161eff701110bc2db4861f7c056f.jpg']")
    btn_img3 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/b5718a64497cb3ec1b5163d1e542cf97.jpg']")

    btn_img4 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/d8d8c1542a4de4d8a40e55ea515f3510.jpg']")
    btn_img5 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/20d8224e2251ac8d96cac98a9c5f76ad.jpg']")
    btn_img6 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/6c47229579bada8d0168322ce65799cb.jpg']")

    btn_img7 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/34f53f55470eba6c082aab72ffcc2aa3.jpg']")
    btn_img8 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/5a2edac72bb93c4186f72382efdfdf8c.jpg']")
    btn_img9 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/3d0eb39d15757c85a1d2527fe22ea312.jpg']")

    btn_img10 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/77abd7081d0a1b97b76b803f750f0d5b.jpg']")
    btn_img11 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/adb802c0dad5311c8b93f3861a8c09b2.jpg']")
    btn_img12 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/4e3d7567ff027676f2769a775ad2cd55.jpg']")

    btn_img13 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/dd80213286305c4375a76d0dde62b905.jpg']")
    btn_img14 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/9d0d9571faaad6152dc5ffd5e2ee3747.jpg']")
    btn_img15 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/55b3f8e129045ae9c9d860b08774610d.jpg']")

    btn_img16 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/bcf2933c661a20f243f03f0596f83412.jpg']")
    btn_img17 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/936b0cc04c9f800b5f96df4031cc3cde.jpg']")
    btn_img18 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/86104e0dde1227fc31cb045e84675fb9.jpg']")

    btn_img19 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/8baa40db8d4a89aa995574306248ac3e.jpg']")
    btn_img20 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/f1bf76a4547c5485d9013f694718cf60.jpg']")
    btn_img21 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/c692b026502b2850fdbb982376134ef4.jpg']")

    btn_img22 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/718543b7dbb59bcf5251690cb133facf.jpg']")
    btn_img23 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/605368abd3e1450ef20975dea8caa550.jpg']")
    btn_img24 = WebElement(xpath="//a[@href = 'https://nie.v.netease.com/nie/2021/0628/f00673f92c13743cebcdbe3803c524ff.jpg']")