from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_PAGE_TITLE = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    BUTTON_START_WINDOW_ENTER = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    BUTTON_DESIGNER = (By.XPATH, ".//p[text()= 'Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH, ".//p[text()= 'Лента Заказов']")
    BUTTON_MAKING_AN_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    BUTTON_CLOSE_WINDOW_IDENTIFICATION_ORDER = (By.XPATH, ".//button[contains(@class, 'close')]")
    CROSS_WINDOW_IGREDIENT = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text() = 'Детали ингредиента']")
    SOUS_SPICY = (By.XPATH, ".//a[contains(@href, 'aaa72')]")
    FLYOR_BUN = (By.XPATH, ".//a[contains(@href, 'aaa6d')]")
    DROP_LOCATOR_UP = (By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']")
    DROP_LOCATOR_DOWN = (By.XPATH, ".//span[text() = 'Перетяните булочку сюда (низ)']")
    COUNT_FLYOR_BUNS = (By.XPATH, ".//ul[contains(@class, '2A-mT')][1]/child::a[1]//p[contains(@class, '3nue1')]")
    ORDER_INGREDIENT = (By.XPATH, ".//span[class = 'constructor-element__text']")
    ORDER_NUMBER = (By.XPATH, ".//div/h2[contains (@class, 'title_shadow')]")
    IDENTIFICATION_ORDER = (By.XPATH, ".//p[text() = 'идентификатор заказа']")
    ELEMENT = (By.XPATH, './/div[@class= "Modal_modal_overlay__x2ZCr"]/parent::div')
    ELEMENT_ORDER = (By.XPATH, ".//img[contains(@class, 'Modal_modal__loading')]")
