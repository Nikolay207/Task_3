from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
EYE_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
PASSWORD_FIELD_WRAPPER = (By.XPATH, "//label[text()='Пароль']/parent::div")