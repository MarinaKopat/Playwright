import allure
import re
import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from playwright.sync_api import Page, expect

URL = "http://localhost:3000/login"
ADMIN_URL = "http://localhost:3000/admin"


@pytest.mark.only
@allure.feature("Админ-панель")
@allure.story("Проверка прав доступа")
class TestAdminExpect:

    @allure.title("Доступ админа к панели управления")
    def test_admin_expect_allowed(self, page):
        login_page = LoginPage(page)
        admin_page = AdminPage(page)

        with allure.step(f"Открытие страницы {URL}"):
            login_page.open(URL)

        with allure.step("Авторизация под админом"):
            login_page.login("admin@example.com", "admin123")
            page.wait_for_timeout(5000)

        with allure.step("Проверка видимости заголовка админки"):
            expect(admin_page.header).to_be_visible(), "Заголовок админ-панели не найден!"

    @allure.title("Запрет доступа для не-админа")
    def test_non_admin_expect_denied(self, page):
        login_page = LoginPage(page)
        admin_page = AdminPage(page)

        with allure.step(f"Открытие страницы {URL}"):
            login_page.open(URL)

        with allure.step("Авторизация обычного пользователя"):
            login_page.login("diana@example.com", "password123")

        with allure.step("Попытка прямого перехода в админку"):
            admin_page.open(ADMIN_URL)

        with allure.step("Проверка отсутствия доступа"):
            expect(admin_page.header).not_to_be_visible(), "Обычный пользователь увидел админку!"
            expect(page).not_to_have_url(re.compile(r"admin"))
