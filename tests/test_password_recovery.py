import allure
import urls
from locators.recovery_password_locators import RecoveryPasswordLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.main_page_locators import MainPageLocators


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_transition_entrance_page_through_button(self, main_page, entrance_page, recovery_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        entrance_page.open_entrance_page()
        entrance_page.click_button_recovery_password()
        recovery_page.wait_element_visibility_of_element(10, RecoveryPasswordLocators.TITLE_PASSWORD_RECOVERY)
        assert recovery_page.find_element(
            RecoveryPasswordLocators.TITLE_PASSWORD_RECOVERY).text == 'Восстановление пароля'

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_button(self, main_page, entrance_page, recovery_page, registration_user, reset_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        entrance_page.open_entrance_page()
        entrance_page.click_button_recovery_password()
        recovery_page.enter_email(registration_user[1])
        recovery_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        recovery_page.click_button_recovery()
        reset_page.wait_element_visibility_of_element(10, ResetPasswordPageLocators.PLACEHOLDER_PASSWORD)
        assert reset_page.get_current_url() == f'{urls.BASE_PAGE}{urls.ENDPOINT_RESET_PASSWORD}'

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным - подсвечивает его')
    def test_click_button_show_and_hide_password(self, main_page, entrance_page, recovery_page, reset_page):
        main_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        entrance_page.open_entrance_page()
        entrance_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        entrance_page.click_button_recovery_password()
        recovery_page.wait_element_element_to_be_clickable(10, RecoveryPasswordLocators.BUTTON_RECOVERY)
        recovery_page.click_button_recovery()
        reset_page.wait_element_element_to_be_clickable(10, ResetPasswordPageLocators.BUTTON_SHOW_AND_HIDE_PASSWORD)
        reset_page.wait_element_invisibility_of_element(10, MainPageLocators.ELEMENT)
        reset_page.click_button_show_and_hide_password()
        assert reset_page.is_password_field_active()
