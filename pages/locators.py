from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocator():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages :first-child")
    BASKET_TOTAL_COST_MSG = (By.CSS_SELECTOR, "#messages .alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    ADDED_TO_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ADDED_TO_BASKET_ITEM_NAME = (By.CSS_SELECTOR, "#messages :first-child strong")