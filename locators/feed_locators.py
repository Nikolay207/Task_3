from selenium.webdriver.common.by import By

FIRST_ORDER_CARD = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]//a)[1]")
FIRST_ORDER_NUMBER = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]//h2)[1]")
ORDER_MODAL_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//p[contains(text(), '#')]")
ORDER_MODAL_STATUS = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//p[contains(text(), 'Выполнен')]")
COUNTER_ALL_TIME = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")
COUNTER_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
READY_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")