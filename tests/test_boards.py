import allure
import pytest
from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from playwright.sync_api import expect

URL = "http://localhost:3000/boards"


@pytest.mark.only
@allure.feature("Управление досками")
def test_boards_elements(page):
    boards_page = BoardsPage(page)
    login_page = LoginPage(page)

    login_page.open(URL)
    login_page.login("diana@example.com", "password123")

    boards_page.open_sidebar_all_boards()

    with allure.step("Проверка наличия задач у пользователя"):
        rows = boards_page.get_boards_rows_locator()
        expect(rows).not_to_have_count(0)

    allure.attach(
        page.screenshot(),
        name="Boards_Screen",
        attachment_type=allure.attachment_type.PNG
    )
