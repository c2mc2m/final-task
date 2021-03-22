from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    page.open()
    page.should_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_info_about_adding()
