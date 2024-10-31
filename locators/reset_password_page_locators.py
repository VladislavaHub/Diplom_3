from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    BUTTON_SHOW_AND_HIDE_PASSWORD = (By.XPATH, ".//div[contains(@class, 'icon-action')]")
    PLACEHOLDER_PASSWORD_STATUS_ACTIVE = (By.XPATH, ".//div[contains(@class, 'status_active')]")
    PLACEHOLDER_PASSWORD = (By.XPATH, ".//div[contains(@class, 'type_password')]")

    status_active = 'class ="input pr-6 pl-6 input_type_password input_size_default input_status_active"'