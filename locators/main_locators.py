from selenium.webdriver.common.by import By

PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
FIRST_INGREDIENT_CARD = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
FIRST_INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')]//div[contains(@class, 'counter_counter')])[1]")
INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")