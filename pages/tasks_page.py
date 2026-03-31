import allure
from .base_page import BasePage


class BoardsPage(BasePage):
    SIDEBAR_TASKS = '[data-qa="sidebar-tasks-link"]'
    TASKS_TABLE_ROWS = "table tbody tr"

    @allure.step("Получить количество задач в таблице")
    def get_tasks_count(self):
        return self.page.locator(self.TASKS_TABLE_ROWS).count()
