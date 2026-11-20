from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
import allure

@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main()
        main_page.click_login_account()
        login_page.go_to_recovery()
        login_page.wait_url_contains("/forgot-password")
        assert "/forgot-password" in driver.current_url, "Не перешли на страницу восстановления пароля"

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_recover(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.open_main()
        main_page.click_login_account()
        login_page.go_to_recovery()
        recovery_page.enter_email(user["email"])
        recovery_page.click_recover()
        recovery_page.wait_url_contains("/reset-password")
        assert "/reset-password" in driver.current_url, "Не перешли на страницу сброса пароля"

    @allure.title('Клик по кнопке показать/скрыть пароль подсвечивает поле')
    def test_toggle_password_visibility(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.open_main()
        main_page.click_login_account()
        login_page.go_to_recovery()
        recovery_page.enter_email(user["email"])
        recovery_page.click_recover()
        recovery_page.wait_url_contains("/reset-password")
        classes_before = recovery_page.get_password_field_classes()
        recovery_page.click_eye_icon()
        classes_after = recovery_page.get_password_field_classes()
        assert classes_before != classes_after, "Поле пароля не подсветилось после клика по глазу"