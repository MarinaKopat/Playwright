import allure
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = "//input[@type='email' or contains(@placeholder, 'Email')]"
    PASSWORD_FIELD = "//input[@type='password' or contains(@placeholder, 'Пароль')]"
    LOGIN_BUTTON = "//button"

    @allure.step("Авторизация пользователем {email}")
    def login(self, email, password):
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
