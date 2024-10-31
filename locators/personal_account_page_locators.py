from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    BUTTON_PROFILE = (By.XPATH, ".//a[text() = 'Профиль']")
    BUTTON_HISTORY_ORDERS = (By.XPATH, ".//a[text() = 'История заказов']")
    BUTTON_HISTORY_ORDERS_ACTIVE = (By.XPATH, ".//a[contains(@class, 'link_active')]")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    ORDER_HISTORY = (By.XPATH, ".//li[last()]/a[contains(@href, 'order-history')]/*/p[1]")
