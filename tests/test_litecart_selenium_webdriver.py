from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

import config


class TestLiteCartUsingSeleniumWebdriver:
    def test_1(self, browser_management_selenium):
        '''
        1. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех блоков (li) с информацией
        о товарах (каждому товару соответствует свой блок)
        '''
        driver = browser_management_selenium
        driver.get(config.settings.base_url)

        all_elements = driver.find_elements(By.CSS_SELECTOR, '.product')

        assert len(all_elements) == 11


    def test_2(self, browser_management_selenium):
        '''
        2. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех ссылок (a) на страницы
        товаров в основной части страницы (не считая боковых блоков)
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url)

        all_links = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.product a.link'))

        assert len(all_links) == 11
        driver.get(all_links[1].get_attribute('href'))
        wait.until(element_to_be_clickable((By.CSS_SELECTOR, 'button[name=add_cart_product]')))

    def test_3(self, browser_management_selenium):
        '''
        3. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ ссылки на Privacy Policy
        в нижней части страницы
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url)

        link = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#footer a[href*=privacy-policy]')).get_attribute('href')
        driver.get(link)
        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'h1')).text

        assert text == 'Privacy Policy'

    def test_4(self, browser_management_selenium):
        '''
        4. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех элементов верхнего меню,
        находящихся на верхнем уровне (без элементов вложенных выпадающих меню)
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url)

        all_elements = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '#site-menu>*>li'))

        assert len(all_elements) == 2

    def test_5_6(self, browser_management_selenium):
        '''
        5. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/create_account элемента
        с текстом United States из выпадающего списка стран
        6. На странице http://litecart.stqa.ru/index.php/en/create_account выберите страну United States и подберите
        локатор для выпадающего списка штатов
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url + '/create_account')

        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '[id^=select2-country_code]')).click()
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '[id^=select2-country_code][id$=US]')).click()
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'select[name=zone_code]')).click()
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'option[value=FL]')).click()

        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '[id^=select2-country_code]')).text
        assert text == 'United States'

    def test_7(self, browser_management_selenium):
        '''
        7. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ кнопки
        сортировки товаров по дате
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url + '/acme-corp-m-1/')

        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'a[href*="sort=date"]')).click()
        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.button.active')).text

        assert text == 'Date'

    def test_8(self, browser_management_selenium):
        '''
        8.Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ иконки-лупы
        для увеличения картинки товара, имеющего стикер Sale
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url + '/acme-corp-m-1/')

        wait.until(lambda driver: driver.find_element(By.XPATH, '//*[contains(@class, "sticker") and contains(@class, "sale")]/../../../*[contains(@class, "zoomable")]')).click()

        wait.until(element_to_be_clickable((By.CSS_SELECTOR, '#fancybox-close')))

    def test_9(self, browser_management_selenium):
        '''
        9. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ всех ссылок на
        товары, у которых нет стикера Sale
        '''
        driver = browser_management_selenium
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
        driver.get(config.settings.base_url + '/acme-corp-m-1/')

        all_elements = wait.until(lambda driver: driver.find_elements(By.XPATH, '//li[contains(@class, "product")][not(.//*[contains(@class, "sale")])]//a[contains(@class, "link")]'))

        assert len(all_elements) == 4

    # def test_10(self, browser_management_selenium):
    #     '''
    #     10. Добавьте в магазине http://litecart.stqa.ru/index.php/en/ в корзину 2-3 товара, перейдите на страницу
    #     оформления заказа http://litecart.stqa.ru/index.php/en/checkout и подберите локатор для поиска элемента,
    #     содержащего общую сумму к оплате
    #     '''
    #     driver = browser_management_selenium
    #     wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
    #     driver.get(config.settings.base_url)
    #
    #     # Добавляем первую утку
    #     browser.all('.product .link').element_by(have.attribute('title').value('Purple Duck')).click()
    #     browser.element('[name=add_cart_product]').click()
    #     browser.element('#cart .quantity').with_(timeout=6).should(have.text('1'))
    #     browser.element('#page #breadcrumbs').element('//a[contains(text(),"Home")]').click()
    #
    #     # Добавляем вторую утку
    #     browser.all('.product .link').element_by(have.attribute('title').value('Green Duck')).click()
    #     browser.element('[name=add_cart_product]').click()
    #     browser.element('#cart .quantity').with_(timeout=6).should(have.text('2'))
    #
    #     # Открываем корзину
    #     browser.element('#cart').click()
    #     browser.element('.dataTable .footer').all('td')[1].should(have.exact_text('$20.00'))

