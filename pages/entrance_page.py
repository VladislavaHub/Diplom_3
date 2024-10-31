import urls
from locators.input_page_locators import InputPageLocators
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class EntrancePage(BasePage):
    @allure.step('Вход в аккаунт')
    def open_entrance_page(self):
        self.open_url(f'{urls.BASE_PAGE}{urls.ENDPOINT_ENTRANCE_PAGE}')
        self.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        self.wait_element_visibility_of_element(10, InputPageLocators.TITLE_ENTRANCE)

    @allure.step('Заполнение поля email')
    def enter_email_entrance_page(self, email):
        self.send_keys(InputPageLocators.PLACEHOLDER_EMAIL, email)

    @allure.step('Заполнение поля пароль')
    def enter_password_entrance_page(self, password):
        self.send_keys(InputPageLocators.PLACEHOLDER_PASSWORD, password)

    @allure.step('Клик по кнопке восстановить пароль')
    def click_button_recovery_password(self):
        self.click_element(InputPageLocators.BUTTON_PASSWORD_RECOVERY)

    @allure.step('Клик по кнопке "Вход"')
    def click_button_entrance(self):
        self.click_element(InputPageLocators.BUTTON_ENTER)
