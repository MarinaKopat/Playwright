import allure
from .base_page import BasePage


class BoardsPage(BasePage):
    SIDEBAR_BOARDS = '[data-qa="sidebar-boards-link"]'
    BOARDS_TABLE_ROWS = "table tbody tr"

    @allure.step("Открыть все доски через сайдбар")
    def open_sidebar_all_boards(self):
        self.page.click(self.SIDEBAR_BOARDS)

    @allure.step("Получить локатор строк таблицы досок")
    def get_boards_rows_locator(self):
        return self.page.locator(self.BOARDS_TABLE_ROWS)
