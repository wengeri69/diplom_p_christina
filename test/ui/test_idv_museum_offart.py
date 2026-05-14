import time
import allure
from conftest import web_browser
import pytest_check as check
from locators.locators_idv_museum_offart import Idv_museum_offart


@allure.title('тесты музея')
def test_museum(web_browser):
    page = Idv_museum_offart(web_browser)
    page.btn_art_museum.click()
    page.btn_more.click()
    for i in range (3):
        page.scroll_down(800)
        time.sleep(2)
    #добавить так чтобы музей картинок листался вниз плавно так чтобы можно было все проверить

        elements = [
            (page.btn_img1, 'img1', 'https://nie.v.netease.com/nie/2021/0628/2489f8d015797103167e4ebed5f4c2bd.jpg'),
            (page.btn_img2, 'img2', 'https://nie.v.netease.com/nie/2021/0628/ac03161eff701110bc2db4861f7c056f.jpg'),
            (page.btn_img3, 'img3', 'https://nie.v.netease.com/nie/2021/0628/b5718a64497cb3ec1b5163d1e542cf97.jpg'),
            (page.btn_img4, 'img4', 'https://nie.v.netease.com/nie/2021/0628/d8d8c1542a4de4d8a40e55ea515f3510.jpg'),
            (page.btn_img5, 'img5', 'https://nie.v.netease.com/nie/2021/0628/20d8224e2251ac8d96cac98a9c5f76ad.jpg'),
            (page.btn_img6, 'img6', 'https://nie.v.netease.com/nie/2021/0628/6c47229579bada8d0168322ce65799cb.jpg'),
            (page.btn_img7, 'img7', 'https://nie.v.netease.com/nie/2021/0628/34f53f55470eba6c082aab72ffcc2aa3.jpg'),
            (page.btn_img8, 'img8', 'https://nie.v.netease.com/nie/2021/0628/5a2edac72bb93c4186f72382efdfdf8c.jpg'),
            (page.btn_img9, 'img9', 'https://nie.v.netease.com/nie/2021/0628/3d0eb39d15757c85a1d2527fe22ea312.jpg'),
            (page.btn_img10, 'img10', 'https://nie.v.netease.com/nie/2021/0628/77abd7081d0a1b97b76b803f750f0d5b.jpg'),
            (page.btn_img11, 'img11', 'https://nie.v.netease.com/nie/2021/0628/adb802c0dad5311c8b93f3861a8c09b2.jpg'),
            (page.btn_img12, 'img12', 'https://nie.v.netease.com/nie/2021/0628/4e3d7567ff027676f2769a775ad2cd55.jpg'),
            (page.btn_img13, 'img13', 'https://nie.v.netease.com/nie/2021/0628/dd80213286305c4375a76d0dde62b905.jpg'),
            (page.btn_img14, 'img14', 'https://nie.v.netease.com/nie/2021/0628/9d0d9571faaad6152dc5ffd5e2ee3747.jpg'),
            (page.btn_img15, 'img15', 'https://nie.v.netease.com/nie/2021/0628/55b3f8e129045ae9c9d860b08774610d.jpg'),
            (page.btn_img16, 'img16', 'https://nie.v.netease.com/nie/2021/0628/bcf2933c661a20f243f03f0596f83412.jpg'),
            (page.btn_img17, 'img17', 'https://nie.v.netease.com/nie/2021/0628/936b0cc04c9f800b5f96df4031cc3cde.jpg'),
            (page.btn_img18, 'img18', 'https://nie.v.netease.com/nie/2021/0628/86104e0dde1227fc31cb045e84675fb9.jpg'),
            (page.btn_img19, 'img19', 'https://nie.v.netease.com/nie/2021/0628/8baa40db8d4a89aa995574306248ac3e.jpg'),
            (page.btn_img20, 'img20', 'https://nie.v.netease.com/nie/2021/0628/f1bf76a4547c5485d9013f694718cf60.jpg'),
            (page.btn_img21, 'img21', 'https://nie.v.netease.com/nie/2021/0628/c692b026502b2850fdbb982376134ef4.jpg'),
            (page.btn_img22, 'img22', 'https://nie.v.netease.com/nie/2021/0628/718543b7dbb59bcf5251690cb133facf.jpg'),
            (page.btn_img23, 'img23', 'https://nie.v.netease.com/nie/2021/0628/605368abd3e1450ef20975dea8caa550.jpg'),
            (page.btn_img24, 'img24', 'https://nie.v.netease.com/nie/2021/0628/f00673f92c13743cebcdbe3803c524ff.jpg'),
            (page.btn_return, 'return', 'https://www.identityvgame.com/index.html?re=1'),
            (page.btn_logo, 'logo', 'https://www.identityvgame.com/index.html?re=1'),
        ]

        for btn, txt, href in elements:
            check.is_true(btn.is_clickable(), f'Элемент {txt} не кликабелен')
            check.is_true(btn.is_presented(), f'Элемента {txt} нет в DOM дереве')
            check.is_true(btn.is_visible(), f'Элемент {txt} не виден на экране')
            check.equal(btn.get_attribute('href'), href, f'Неверная ссылка в {txt}')
            check.equal(btn.get_text(), txt, f'Неверный текст в {txt}')
