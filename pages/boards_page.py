import allure
from .base_page import BasePage


class BoardsPage(BasePage):
    SIDEBAR_BOARDS = '[data-qa="sidebar-boards-link"]'
    BOARDS_TABLE_ROWS = "table tbody tr"

    @allure.step("Получить количество досок в таблице")
    def get_boards_count(self):
        return self.page.locator(self.BOARDS_TABLE_ROWS).count()
