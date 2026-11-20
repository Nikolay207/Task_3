from pages.base_page import BasePage
from locators import account_locators
import allure


class AccountPage(BasePage):

    @allure.step('Переходим в историю заказов')
    def go_to_order_history(self):
        self.click_js(account_locators.ACCOUNT_HISTORY_BUTTON)

    @allure.step('Выходим из аккаунта')
    def logout(self):
        self.click_js(account_locators.LOGOUT_BUTTON)