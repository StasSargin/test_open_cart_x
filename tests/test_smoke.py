from TestX.page_objects import HeaderPage, ProductPage, CartPage


def test_smoke(browser):
    HeaderPage(browser)\
        .click_category()\
        .click_product()
    ProductPage(browser)\
        .add_product_to_cart()\
        .verify_success_alert()\
        .click_cart_total()\
        .click_view_cart()
    CartPage(browser)\
        .checkout_click()
