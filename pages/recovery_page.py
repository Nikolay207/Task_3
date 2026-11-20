from pages.base_page import BasePage
from locators import recovery_locators
import allure


class RecoveryPage(BasePage):
    @allure.step('Вводим email')
    def enter_email(self, email):
        self.add_text_to_element(recovery_locators.EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку «Восстановить»')
    def click_recover(self):
        self.click_js(recovery_locators.RECOVER_BUTTON)

    @allure.step('Кликаем по иконке глаза (показать/скрыть пароль)')
    def click_eye_icon(self):
        self.click_js(recovery_locators.EYE_ICON)

    @allure.step('Получаем классы обёртки поля пароля')
    def get_password_field_classes(self):
        element = self.find_element_with_wait(recovery_locators.PASSWORD_FIELD_WRAPPER)
        return element.get_attribute("class")