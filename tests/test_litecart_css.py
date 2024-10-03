from selene import browser, query, have, be


class TestLiteCart:
    def test_1(self):
        # 1. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех блоков (li) с информацией
        # о товарах (каждому товару соответствует свой блок)
        browser.open('/')

        browser.all('.product').should(have.size(11))

    def test_2(self):
        # 2. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех ссылок (a) на страницы
        # товаров в основной части страницы (не считая боковых блоков)
        browser.open('/')

        all_links = browser.all('.product a.link')

        all_links.should(have.size(11))
        browser.open(all_links[1].get(query.attribute('href')))
        browser.element('button[name=add_cart_product]').should(be.clickable)

    def test_3(self):
        # 3. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ ссылки на Privacy Policy
        # в нижней части страницы
        browser.open('/')
        link = browser.element('#footer a[href*=privacy-policy]').get(query.attribute('href'))
        browser.open(link)
        browser.element('h1').should(have.exact_text('Privacy Policy'))

    def test_4(self):
        # 4. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех элементов верхнего меню,
        # находящихся на верхнем уровне (без элементов вложенных выпадающих меню)
        browser.open('/')
        browser.all('#site-menu>*>li').should(have.size(2))

    def test_5_6(self):
        # 5, 6 United States
        # 5. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/create_account элемента
        # с текстом United States из выпадающего списка стран
        # 6. На странице http://litecart.stqa.ru/index.php/en/create_account выберите страну United States и подберите
        # локатор для выпадающего списка штатов
        browser.open('/create_account')

        browser.element('[id^=select2-country_code]').click()
        browser.element('[id^=select2-country_code][id$=US]').click()
        browser.element('select[name=zone_code]').click()
        browser.element('option[value=FL]').click()

        browser.element('[id^=select2-country_code]').should(have.exact_text('United States'))

    def test_7(self):
        # 7. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ кнопки
        # сортировки товаров по дате
        browser.open('/acme-corp-m-1/')

        browser.element('a[href*="sort=date"]').click()

        browser.element('.button.active').should(have.exact_text('Date'))

    def test_8(self):
        # 8.Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ иконки-лупы
        # для увеличения картинки товара, имеющего стикер Sale
        browser.open('/acme-corp-m-1/')

        browser.element('.sticker.sale').element('../../..').element('.zoomable').click()

        browser.element('#fancybox-close').should(be.clickable)

    def test_9(self):
        # 9. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ всех ссылок на
        # товары, у которых нет стикера Sale
        browser.open('/acme-corp-m-1/')

        browser.all('.product .link').by_their('.image-wrapper>div', have.no.css_class('sale')).should(have.size(4))


    def test_10(self):
        # 10. Добавьте в магазине http://litecart.stqa.ru/index.php/en/ в корзину 2-3 товара, перейдите на страницу
        # оформления заказа http://litecart.stqa.ru/index.php/en/checkout и подберите локатор для поиска элемента,
        # содержащего общую сумму к оплате
        browser.open('/')

        # Добавляем первую утку
        browser.all('.product .link').element_by(have.attribute('title').value('Purple Duck')).click()
        browser.element('[name=add_cart_product]').click()
        browser.element('#cart .quantity').with_(timeout=6).should(have.text('1'))
        browser.element('#page #breadcrumbs').element('//a[contains(text(),"Home")]').click()

        # Добавляем вторую утку
        browser.all('.product .link').element_by(have.attribute('title').value('Green Duck')).click()
        browser.element('[name=add_cart_product]').click()
        browser.element('#cart .quantity').with_(timeout=6).should(have.text('2'))

        # Открываем корзину
        browser.element('#cart').click()
        browser.element('.dataTable .footer').all('td')[1].should(have.exact_text('$20.00'))

