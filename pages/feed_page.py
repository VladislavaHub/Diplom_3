import allure
from locators.main_page_locators import MainPageLocators
from locators.feed_locators import FeedLocators
import urls
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Открываем страницу ленты заказов')
    def open_url_order_feed(self):
        self.open_url(f'{urls.BASE_PAGE}{urls.ENDPOINT_ORDER_FEED}')
        self.wait_element_visibility_of_element(10, FeedLocators.ORDER_FEED_TITLE)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_button_designer(self):
        self.click_element(MainPageLocators.BUTTON_DESIGNER)

    @allure.step('Нажимаем на заказ')
    def click_order(self):
        self.click_element(FeedLocators.ORDER)

    @allure.title('Получение заказа в листе заказов')
    def search_order_feed_list(self):
        return self.get_text(FeedLocators.ORDER_FEED)

    @allure.step('Получение количество счётчика Выполнено за всё время')
    def get_text_order_all_time(self):
        result = self.get_text(FeedLocators.SUCCESSFULLY_ALL_TIME)
        return result

    @allure.step('Получение количество счётчика Выполнено за сегодня')
    def get_text_order_today_time(self):
        result = self.get_text(FeedLocators.SUCCESSFULLY_TODAY_TIME)
        return result

    @allure.step('Получение заказа в списке "В работе"')
    def get_order_list_in_job(self):
        return self.get_text(FeedLocators.ORDER_IN_PROGRESS)
