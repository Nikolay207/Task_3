from selenium.webdriver.common.by import By

ACCOUNT_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
HISTORY_PAGE_HEADER = (By.XPATH, "//h2[contains(text(), 'История заказов')]")
HISTORY_ORDER_NUMBER = (By.XPATH, "(//p[contains(text(), '#')])[1]")