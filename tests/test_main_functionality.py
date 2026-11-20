from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators import main_locators
import allure


@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Переход в конструктор по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_order_feed()
        main_page.wait_url_contains("/feed")
        main_page.click_constructor()
        assert main_page.check_element_is_displayed(main_locators.FIRST_INGREDIENT_CARD), \
            "Не открылся конструктор"

    @allure.title('Переход в ленту заказов по клику на «Лента Заказов»')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_order_feed()
        main_page.wait_url_contains("/feed")
        assert "/feed" in driver.current_url, "Не перешли в ленту заказов"

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_first_ingredient()
        assert main_page.check_element_is_displayed(main_locators.INGREDIENT_MODAL_TITLE), \
            "Не открылось окно с деталями ингредиента"

    @allure.title('Окно ингредиента закрывается по крестику')
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.click_first_ingredient()
        assert main_page.check_element_is_displayed(main_locators.INGREDIENT_MODAL_TITLE), \
            "Окно ингредиента не открылось"
        main_page.close_modal()
        assert main_page.is_element_invisible(main_locators.INGREDIENT_MODAL_TITLE), \
            "Окно ингредиента не закрылось после клика по крестику"

    @allure.title('Счётчик ингредиента отображается на карточке')
    def test_ingredient_counter_exists(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        counter = main_page.get_first_ingredient_counter()
        assert counter.isdigit(), f"Счётчик не число: {counter}"

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_make_order(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_main()
        main_page.click_login_account()
        login_page.login(user["email"], user["password"])
        assert main_page.is_user_logged_in(), "Пользователь не авторизовался"
        assert main_page.check_element_is_displayed(main_locators.MAKE_ORDER_BUTTON), \
            "Кнопка «Оформить заказ» недоступна залогиненному пользователю"