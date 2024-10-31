from selenium.webdriver.common.by import By


class InputPageLocators:

    TITLE_ENTRANCE = (By.XPATH, ".//h2[text() = 'Вход']")
    BUTTON_ENTER = (By.XPATH, ".//button[text() = 'Войти']")
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()= 'Восстановить пароль']")
    PLACEHOLDER_EMAIL = (By.NAME, "name")
    PLACEHOLDER_PASSWORD = (By.NAME, "Пароль")


