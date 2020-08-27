from TestX.locators import Cart
from .BasePage import BasePage


class CartPage(BasePage):
    def checkout_click(self):
        self._click(selector=Cart.checkout_button)
