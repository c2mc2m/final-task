from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), \
            "The basket is not empty"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_LIST), \
            "There are items in the basket, but should not be"