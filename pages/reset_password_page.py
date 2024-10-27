import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_button_show_and_hide_password(self):
        self.click_element(ResetPasswordPageLocators.BUTTON_SHOW_AND_HIDE_PASSWORD)

    @allure.step('Проверим, что поле  активно')
    def is_password_field_active(self):
        return self.element_visibility(ResetPasswordPageLocators.PLACEHOLDER_PASSWORD_STATUS_ACTIVE)
