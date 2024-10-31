import allure

from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Заполняем поле Email')
    def enter_email(self, email):
        self.send_keys(RecoveryPasswordLocators.PLACEHOLDER_EMAIL, email)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_button_recovery(self):
        self.click_element(RecoveryPasswordLocators.BUTTON_RECOVERY)
