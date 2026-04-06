import allure
import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

URL = "http://localhost:3000/dashboard"


@pytest.mark.only
@allure.feature("Панель управления")
@allure.story("Проверка основных элементов дашборда")
@allure.title("Успешная проверка счетчиков и навигации")
def test_dashboard_elements(page):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    page.goto(URL)
    login_page.login("diana@example.com", "password123")

    with allure.step("Проверка количества досок"):
        expect(dashboard.boards_count).not_to_have_text("0")

        with allure.step("Проверка количества задач"):
            expect(dashboard.total_tasks_count).not_to_have_text("0")

        with allure.step("Проверка количества задач в работе"):
            expect(dashboard.in_progress_count).not_to_have_text("0")

        with allure.step("Проверка количества выполненных задач"):
            expect(dashboard.done_count).not_to_have_text("0")

        with allure.step("Проверка видимости кнопки создания"):
            expect(dashboard.create_board_btn).to_be_visible()

        expected_name = "diana"
        with allure.step(f"Проверка, что имя пользователя соответствует {expected_name}"):
            expect(dashboard.username_label).to_have_text(expected_name)
