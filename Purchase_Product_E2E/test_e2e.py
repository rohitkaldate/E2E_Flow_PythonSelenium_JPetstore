from Purchase_Product_E2E.add_to_cart import AddToCart
from Purchase_Product_E2E.checkout import Checkout
from Purchase_Product_E2E.confirm_purchase import Confirmation
from Purchase_Product_E2E.launch import LaunchPage
from Purchase_Product_E2E.login import LoginApp
from Purchase_Product_E2E.logout import Logout


def test_e2e_demo(browserInstance):
    #Browser Launch
    driver = browserInstance

    launch =LaunchPage(driver)
    launch.launch_webpage()

    login_info = LoginApp(driver)
    login_info.login_page("standard_user","secret_sauce")

    cart = AddToCart(driver)
    cart.add_to_cart_and_go_to_cart()
    # cart.cart_item()
    checkout = Checkout(driver)
    checkout.checkout()
    confirm = Confirmation(driver)
    confirm.confirm_purchase_product("Jim","Gray",123567)
    confirm.go_back()

    logout = Logout(driver)
    logout.click_sidebar()
    logout.logout_application()

