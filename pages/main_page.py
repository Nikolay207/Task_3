from pages.base_page import BasePage
from locators import main_locators
import allure


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main(self):
        self.go_to_url("https://qa-stellarburgers.education-services.ru/")

    @allure.step('Кликаем по кнопке "Личный Кабинет"')
    def click_personal_account(self):
        self.wait_element_invisible(main_locators.MODAL_OVERLAY)
        self.click_js(main_locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликаем по кнопке "Войти в аккаунт"')
    def click_login_account(self):
        self.wait_element_invisible(main_locators.MODAL_OVERLAY)
        self.click_js(main_locators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Проверяем, что пользователь авторизован')
    def is_user_logged_in(self):
        return self.check_element_is_displayed(main_locators.MAKE_ORDER_BUTTON)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor(self):
        self.click_js(main_locators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем по кнопке "Лента Заказов"')
    def click_order_feed(self):
        self.click_js(main_locators.ORDER_FEED_BUTTON)

    @allure.step('Кликаем по первой карточке ингредиента')
    def click_first_ingredient(self):
        self.click_js(main_locators.FIRST_INGREDIENT_CARD)

    @allure.step('Закрываем модальное окно крестиком')
    def close_modal(self):
        self.click_js(main_locators.MODAL_CLOSE_BUTTON)

    @allure.step('Получаем значение счётчика первого ингредиента')
    def get_first_ingredient_counter(self):
        element = self.find_element_with_wait(main_locators.FIRST_INGREDIENT_COUNTER)
        return element.text

    @allure.step('Нажимаем кнопку «Оформить заказ»')
    def click_make_order(self):
        self.click_js(main_locators.MAKE_ORDER_BUTTON)