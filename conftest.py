import pytest
import requests
from selenium import webdriver
from data import Data
import urls
from locators.input_page_locators import InputPageLocators
from locators.main_page_locators import MainPageLocators
from pages.entrance_page import EntrancePage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.get(urls.BASE_PAGE)
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.get(urls.BASE_PAGE)
    yield browser
    browser.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def entrance_page(driver):
    return EntrancePage(driver)


@pytest.fixture()
def recovery_page(driver):
    return RecoveryPasswordPage(driver)


@pytest.fixture()
def reset_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture()
def personal_account_page(driver):
    return PersonalAccountPage(driver)


@pytest.fixture()
def order_feed_page(driver):
    return FeedPage(driver)


@pytest.fixture()
def registration_user(driver):
    email = Data.DATA_USER_EMAIL
    password = Data.DATA_USER_PASSWORD
    name = Data.DATA_USER_NAME
    registration_user_body = {"email": email, "password": password, "name": name}
    response_reg = requests.post(f'{urls.BASE_PAGE}{urls.REGISTRATION_USER_ENDPOINT}', json=registration_user_body)
    token = response_reg.json()["accessToken"]
    yield [token, email, password, name]
    requests.delete(f'{urls.BASE_PAGE}{urls.DELETE_USER_ENDPOINT}', headers={'Authorization': token})


@pytest.fixture()
def personal_account(driver, registration_user, main_page, entrance_page):
    main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
    main_page.click_button_personal_account()
    entrance_page.wait_element_visibility_of_element(10, InputPageLocators.TITLE_ENTRANCE)
    entrance_page.enter_email_entrance_page(registration_user[1])
    entrance_page.enter_password_entrance_page(registration_user[2])
    entrance_page.click_button_entrance()
    return personal_account
