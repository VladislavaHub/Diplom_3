import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    @allure.step('Создать драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Ожидание наличия элемента на странице')
    def wait_element_presence_of_element_located(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_element_element_to_be_clickable(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Наличие элемента на странице')
    def wait_element_visibility_of_element(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_invisibility_of_element(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Неявное ожидание')
    def wait(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Получение url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ввод текста')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Видимость элемента')
    def element_visibility(self, locator):
        result = True
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            result = False
        return result

    @allure.step('Перетаскивание Элемента')
    def drag_and_drop_elemen(self, source, target):
        source = self.find_element(source)
        target = self.find_element(target)
        return drag_and_drop(self.driver, source, target)
