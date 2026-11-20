from pages.base_page import BasePage
from locators import feed_locators
from selenium.webdriver.common.by import By
import allure

class FeedPage(BasePage):

    @allure.step('Кликаем по первой карточке заказа в ленте')
    def click_first_order(self):
        self.click_js(feed_locators.FIRST_ORDER_CARD)

    @allure.step('Получаем номер первого заказа в ленте')
    def get_first_order_number(self):
        element = self.find_element_with_wait(feed_locators.FIRST_ORDER_NUMBER)
        return element.text.replace("#", "")

    @allure.step('Получаем число из счётчика «Выполнено за все время»')
    def get_all_time_counter(self):
        element = self.find_element_with_wait(feed_locators.COUNTER_ALL_TIME)
        return int(element.text)

    @allure.step('Получаем число из счётчика «Выполнено за сегодня»')
    def get_today_counter(self):
        element = self.find_element_with_wait(feed_locators.COUNTER_TODAY)
        return int(element.text)

    @allure.step('Получаем список номеров готовых заказов')
    def get_ready_orders(self):
        container = self.find_element_with_wait(feed_locators.READY_ORDERS_LIST)
        return [li.text for li in container.find_elements(By.XPATH, ".//li")]