import allure
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = "input[type='email']"
    PASSWORD_FIELD = "input[type='password']"
    LOGIN_BUTTON = "button:has-text('Войти')"

    @allure.step("Авторизация пользователем {email}")
    def login(self, email, password):
        self.page.fill(self.EMAIL_FIELD, email)
        self.page.fill(self.PASSWORD_FIELD, password)
        self.page.click(self.LOGIN_BUTTON)
