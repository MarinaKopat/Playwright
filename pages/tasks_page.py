import allure
from .base_page import BasePage


class TasksPage(BasePage):
    SIDEBAR_TASKS = '[data-qa="sidebar-tasks-link"]'
    TASKS_TABLE_ROWS = "table tbody tr"

    @allure.step("Открыть все задачи через сайдбар")
    def open_sidebar_all_tasks(self):
        self.page.click(self.SIDEBAR_TASKS)

    @allure.step("Получить локатор строк таблицы досок")
    def get_tasks_rows_locator(self):
        return self.page.locator(self.TASKS_TABLE_ROWS)
