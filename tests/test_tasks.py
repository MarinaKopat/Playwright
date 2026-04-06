import allure
import pytest
from pages.login_page import LoginPage
from pages.tasks_page import TasksPage
from playwright.sync_api import Page, expect

URL = "http://localhost:3000/boards"


@pytest.mark.only
@allure.feature("Управление задачами")
def test_tasks_elements(page):
    tasks_page = TasksPage(page)
    login_page = LoginPage(page)

    login_page.open(URL)
    login_page.login("diana@example.com", "password123")

    tasks_page.open_sidebar_all_tasks()

    with allure.step("Проверка наличия задач у пользователя"):
        rows = tasks_page.get_tasks_rows_locator()
        expect(rows).not_to_have_count(0)

    allure.attach(
        page.screenshot(),
        name="Tasks_Screen",
        attachment_type=allure.attachment_type.PNG
    )
