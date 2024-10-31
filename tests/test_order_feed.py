import allure
from locators.feed_locators import FeedLocators
from locators.main_page_locators import MainPageLocators


class TestOrdersFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_opening_an_order_window_with_details(self, main_page, order_feed_page):
        order_feed_page.open_url_order_feed()
        order_feed_page.wait_element_visibility_of_element(10, FeedLocators.ORDER_FEED_TITLE)
        order_feed_page.click_order()
        assert order_feed_page.find_element(FeedLocators.WINDOW_ORDER)

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_displaying_user_orders_in_feeds(self, order_feed_page, personal_account, main_page,
                                             personal_account_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.drag_and_drop_buns()
        main_page.click_button_making_an_order()
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT_ORDER)
        main_page.close_window_identification_order()
        main_page.wait_element_element_to_be_clickable(10, MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        main_page.click_button_personal_account()
        personal_account_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        personal_account_page.transition_to_history_order()
        personal_account_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT_ORDER)
        order_history = personal_account_page.get_text_number_order()
        main_page.click_button_order_feed()
        order_feed_page.wait(FeedLocators.ORDER_FEED_TITLE, 'Лента заказов')
        assert order_history in order_feed_page.search_order_feed_list()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_add_order_counter_all_time_up(self, personal_account, main_page, order_feed_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.click_button_order_feed()
        order_feed_page.wait_element_visibility_of_element(10, FeedLocators.ORDER_FEED_TITLE)
        order_before = order_feed_page.get_text_order_all_time()
        order_feed_page.click_button_designer()
        main_page.drag_and_drop_buns()
        main_page.click_button_making_an_order()
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT_ORDER)
        main_page.close_window_identification_order()
        main_page.click_button_order_feed()
        order_feed_page.wait(FeedLocators.ORDER_FEED_TITLE, 'Лента заказов')
        order_after = order_feed_page.get_text_order_all_time()
        assert order_after > order_before

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_add_order_counter_today_up(self, personal_account, main_page, order_feed_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.click_button_order_feed()
        order_feed_page.wait_element_visibility_of_element(10, FeedLocators.ORDER_FEED_TITLE)
        order_before = order_feed_page.get_text_order_today_time()
        order_feed_page.click_button_designer()
        main_page.drag_and_drop_buns()
        main_page.click_button_making_an_order()
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT_ORDER)
        main_page.close_window_identification_order()
        main_page.click_button_order_feed()
        order_feed_page.wait(FeedLocators.ORDER_FEED_TITLE, 'Лента заказов')
        order_after = order_feed_page.get_text_order_today_time()

        assert order_after > order_before

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_add_order_order_in_progress(self, personal_account, main_page, order_feed_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.drag_and_drop_buns()
        main_page.click_button_making_an_order()
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT_ORDER)
        number = main_page.get_number_order()
        main_page.close_window_identification_order()
        main_page.click_button_order_feed()
        order_feed_page.wait(FeedLocators.ORDER_ON_LIST, '0')
        order_list = order_feed_page.get_order_list_in_job()
        assert number in order_list
