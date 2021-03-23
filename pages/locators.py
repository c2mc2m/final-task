from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[value=Register]")

class ProductPageLocator():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages :first-child")
    BASKET_TOTAL_COST_MSG = (By.CSS_SELECTOR, "#messages .alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    ADDED_TO_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ADDED_TO_BASKET_ITEM_NAME = (By.CSS_SELECTOR, "#messages :first-child strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators(): 
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM_LIST = (By.CSS_SELECTOR, "#basket-formset")