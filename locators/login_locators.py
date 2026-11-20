from selenium.webdriver.common.by import By

# Локаторы для страницы входа
EMAIL_INPUT = (By.XPATH, "//input[@name='name']")       # поле «Email»
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # поле «Пароль»
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")   # кнопка «Войти»
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")