from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.account_page import AccountPage
from locators import feed_locators, account_locators
import allure


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Клик по заказу открывает окно с деталями')
    def test_order_opens_modal(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        feed.click_first_order()
        assert main.check_element_is_displayed(feed_locators.ORDER_MODAL_NUMBER)

    @allure.title('Заказы из истории есть в ленте')
    def test_history_orders_visible_in_feed(self, driver, user_with_order):
        main = MainPage(driver)
        login = LoginPage(driver)
        account = AccountPage(driver)
        feed = FeedPage(driver)
        main.open_main()
        main.click_login_account()
        login.login(user_with_order["email"], user_with_order["password"])
        assert main.is_user_logged_in(), "Не авторизовался"
        main.click_personal_account()
        account.go_to_order_history()
        order_num = main.get_text_from_element(account_locators.HISTORY_ORDER_NUMBER)
        main.click_order_feed()
        main.wait_url_contains("/feed")
        feed.click_first_order()
        modal_num = main.get_text_from_element(feed_locators.ORDER_MODAL_NUMBER)
        assert order_num in modal_num

    @allure.title('Счётчик «Выполнено за все время» не уменьшается')
    def test_all_time_counter_not_decreases(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        before = feed.get_all_time_counter()
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        assert feed.get_all_time_counter() >= before

    @allure.title('Счётчик «Выполнено за сегодня» не уменьшается')
    def test_today_counter_not_decreases(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        before = feed.get_today_counter()
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        assert feed.get_today_counter() >= before

    @allure.title('В ленте есть номера заказов')
    def test_order_numbers_visible_in_feed(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main()
        main.click_order_feed()
        main.wait_url_contains("/feed")
        assert len(feed.get_ready_orders()) > 0