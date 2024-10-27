import allure

from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    @allure.step('Переход в раздел "История заказов"')
    def transition_to_history_order(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_HISTORY_ORDERS)

    @allure.step('Выход из аккаунта')
    def click_button_exit_account(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_EXIT)

    @allure.step('Получение номера заказа')
    def get_text_number_order(self):
        return self.get_text(PersonalAccountPageLocators.ORDER_HISTORY)
