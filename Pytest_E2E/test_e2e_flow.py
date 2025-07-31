import os
import sys

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Pytest_E2E.Pages.continue_confirm import Confirm
from Pytest_E2E.Pages.launch import Launch
from Pytest_E2E.Pages.login import Login
from Pytest_E2E.Pages.logout import Logout
from Pytest_E2E.Pages.select_product import Product


def test_e2e_flow(browserInstance):
    #Browser Launch
    driver = browserInstance

    #URL to automate
    launch_web = Launch(driver)
    launch_web.launch()

    #Login to app
    login_info = Login(driver)
    login_info.login_details("j2ee","j2ee")

    #Select the product and add to cart
    product = Product(driver)
    product.choose_product()
    product.add_to_cart_and_checkout()

    #Confirm Purchase
    purchase = Confirm(driver)
    purchase.order_product()

    #Logout application
    logout_app = Logout(driver)
    logout_app.logout_application()