from pages.base_page import BasePage
from locators import login_locators
import allure

class LoginPage(BasePage):

    @allure.step('Вводим email')
    def enter_email(self, email):
        self.add_text_to_element(login_locators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.add_text_to_element(login_locators.PASSWORD_INPUT, password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login(self):
        self.click_js(login_locators.LOGIN_BUTTON)

    @allure.step('Авторизуемся с email и паролем')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    @allure.step('Переходим на страницу восстановления пароля')
    def go_to_recovery(self):
        self.click_js(login_locators.FORGOT_PASSWORD_LINK)