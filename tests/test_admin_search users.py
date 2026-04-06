import allure
import pytest
from pages.login_page import LoginPage
from pages.search_users_page import SearchUsers
from playwright.sync_api import expect

URL = "http://localhost:3000/login"
ADMIN_URL = "http://localhost:3000/admin"


@pytest.mark.only
@allure.feature("Административная панель")
@allure.story("Поиск пользователей")
class TestAdminAccess:
    @allure.title("Доступ админа к панели управления")
    def test_admin_open(self, page):
        search_page = SearchUsers(page)
        login_page = LoginPage(page)
        email_to_search = "@example.com"

        with allure.step(f"Открытие страницы {URL}"):
            login_page.open(URL)

        with allure.step("Авторизация под админом"):
            login_page.login("admin@example.com", "admin123")
            search_page.open_administrative_panel()

        with allure.step(f"Выполнение поиска пользователя: {email_to_search}"):
            search_page.search_user(email_to_search)

        with allure.step("Валидация результатов поиска"):
            user_locator = search_page.get_user_row(email_to_search)

            expect(user_locator.first).to_be_visible()
            assert user_locator.count() > 0, f"Email {email_to_search} не найден"

            allure.attach(
                page.screenshot(),
                name="search_result",
                attachment_type=allure.attachment_type.PNG
            )
