from TestX.locators import Product
from .BasePage import BasePage
import time


class ProductPage(BasePage):

    def add_product_to_cart(self):
        time.sleep(2) # Обхожу selenium.common.exceptions.MoveTargetOutOfBoundsException
        self._click(selector=Product.product_buttons)
        return ProductPage(self.driver)

    def verify_success_alert(self):
        assert self._get_element_text(selector=Product.success_alert, index=0)
        return ProductPage(self.driver)

    def click_cart_total(self):
        self._click(selector=Product.cart_total)
        return ProductPage(self.driver)

    def click_view_cart(self):
        self._wait_for_visible(selector=Product.cart_total_buttons)
        self._click(selector=Product.cart_total_buttons)
