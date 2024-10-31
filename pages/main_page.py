import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Клик на ингредиент')
    def click_for_ingredient(self):
        self.click_element(MainPageLocators.FLYOR_BUN)

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Перетаскивание булок')
    def drag_and_drop_buns(self):
        self.driver.implicitly_wait(3)
        self.drag_and_drop_elemen(MainPageLocators.FLYOR_BUN, MainPageLocators.DROP_LOCATOR_UP)

    @allure.title('Перетаскивание соуса')
    def drag_and_drop_souse(self):
        self.driver.implicitly_wait(3)
        self.drag_and_drop_elemen(MainPageLocators.SOUS_SPICY, MainPageLocators.DROP_LOCATOR_UP)

    @allure.step('Получение счётчика ингредиента')
    def get_counter_ingredient(self):
        return self.get_text(MainPageLocators.COUNT_FLYOR_BUNS)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_button_making_an_order(self):
        self.click_element(MainPageLocators.BUTTON_MAKING_AN_ORDER)

    @allure.step('Закрываем окно с идентификатором заказа')
    def close_window_identification_order(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_WINDOW_IDENTIFICATION_ORDER)

    @allure.step('Получение номера заказа')
    def get_number_order(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)
