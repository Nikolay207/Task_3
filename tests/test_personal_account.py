from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure

@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Переход в личный кабинет по клику на кнопку')
    def test_go_to_personal_account(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main()
        main_page.click_login_account()
        login_page.login(user["email"], user["password"])
        assert main_page.is_user_logged_in(), "Пользователь не авторизовался"
        main_page.click_personal_account()
        assert "/account" in driver.current_url, "Не перешли в личный кабинет"