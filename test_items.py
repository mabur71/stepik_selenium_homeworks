import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        # Открываем страницу товара
        browser.get(link)
        
        # Установлено время принудительной задержки браузера
        time.sleep(25)
        
        # Проверяем наличие кнопки добавления товара в корзину
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")

