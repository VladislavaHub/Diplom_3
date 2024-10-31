from selenium.webdriver.common.by import By


class RecoveryPasswordLocators:

    TITLE_PASSWORD_RECOVERY = (By.XPATH, ".//h2[text()= 'Восстановление пароля']")
    PLACEHOLDER_EMAIL = (By.XPATH, ".//input")
    BUTTON_RECOVERY = (By.XPATH, ".//button[text()='Восстановить']")
