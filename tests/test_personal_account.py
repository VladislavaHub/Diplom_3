import allure
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.input_page_locators import InputPageLocators
class TestPersonalAccount:

    @allure.title('Преход по клику на "Личный кабинет"')
    def test_transition_personal_account_by_button(self, main_page, personal_account_page, personal_account):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.click_button_personal_account()
        personal_account_page.wait_element_visibility_of_element(10, PersonalAccountPageLocators.BUTTON_PROFILE)
        assert personal_account_page.find_element(PersonalAccountPageLocators.BUTTON_PROFILE).text == "Профиль"

    @allure.title('Преход в раздел "История заказов"')
    def test_transition_histore_orders(self, main_page, personal_account_page, personal_account):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.wait_element_visibility_of_element(10, MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        main_page.click_button_personal_account()
        personal_account_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        personal_account_page.transition_to_history_order()
        (personal_account_page.wait_element_visibility_of_element
         (10, PersonalAccountPageLocators.BUTTON_HISTORY_ORDERS_ACTIVE))
        assert personal_account_page.find_element(PersonalAccountPageLocators.BUTTON_HISTORY_ORDERS_ACTIVE)

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, main_page, personal_account_page, entrance_page, personal_account):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        main_page.click_button_personal_account()
        personal_account_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        personal_account_page.click_button_exit_account()
        entrance_page.wait(InputPageLocators.TITLE_ENTRANCE, 'Вход')
        assert entrance_page.find_element(InputPageLocators.TITLE_ENTRANCE)
