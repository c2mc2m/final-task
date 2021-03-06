from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def go_to_basket(self):
        self.busket_link = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET_BUTTON)
        self.busket_link.click()

    def is_added_cost_equal_to_price(self):
        assert self.value_compare(ProductPageLocator.ITEM_PRICE, ProductPageLocator.ADDED_TO_BASKET_PRICE), \
            "The prices are not equal"
    
    def is_added_itemname_equal_to_catalogname(self):
        assert self.value_compare(ProductPageLocator.ITEM_NAME, ProductPageLocator.ADDED_TO_BASKET_ITEM_NAME), \
            "The items name are not equal"

    def should_add_to_basket(self):
        self.should_be_button_add_to_basket()
        self.go_to_basket()

    def should_see_info_about_adding(self):
        self.should_see_added_msg()
        self.should_see_cost_msg()
        self.is_added_cost_equal_to_price()
        self.is_added_itemname_equal_to_catalogname()

    def should_be_promo_url(self):
        assert self.is_required_url("?promo="), \
            "The current url is not 'promo' url"
    
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocator.ADD_TO_BASKET_BUTTON), \
            "The ad_to_basket button is absent"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.PRODUCT_ADDED_MSG), \
            "Success message is presented, but should not be"

    def should_not_disappear(self):
        assert self.is_disappeared(*ProductPageLocator.PRODUCT_ADDED_MSG), \
            "The message is disappeared, but shouldt be"

    def should_see_added_msg(self):
        assert self.is_element_present(*ProductPageLocator.PRODUCT_ADDED_MSG), \
            "There is no 'added item' message"

    def should_see_cost_msg(self):
        assert self.is_element_present(*ProductPageLocator.BASKET_TOTAL_COST_MSG), \
            "There is no info-message about the cost of the items in the basket"

        