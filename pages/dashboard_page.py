import allure
from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.page = page
        self.boards_count = page.locator('[data-qa="dashboard-stat-total-boards-value"]')
        self.total_tasks_count = page.locator('[data-qa="dashboard-stat-total-tasks-value"]')
        self.in_progress_count = page.locator('[data-qa="dashboard-stat-in-progress-value"]')
        self.done_count = page.locator('[data-qa="dashboard-stat-done-value"]')
        self.create_board_btn = page.locator('[data-qa="dashboard-create-board-button"]')
        self.username_label = page.locator(".header-username")

    @allure.step("Нажать кнопку создания новой доски")
    def click_create_board(self):
        self.create_board_btn.click()

    @allure.step("Получить количество досок из статистики")
    def get_boards_count(self):
        return self.boards_count.inner_text()

    @allure.step("Получить количество задач из статистики")
    def get_tasks_count(self):
        return self.total_tasks_count.inner_text()

    @allure.step("Получить количество задач в работе из статистики")
    def get_tasks_in_progress_count(self):
        return self.in_progress_count.inner_text()

    @allure.step("Получить количество задач выполнены из статистики")
    def get_tasks_done_count(self):
        return self.done_count.inner_text()

    @allure.step("Проверка видимости кнопки создания")
    def is_create_button_visible(self):
        return self.create_board_btn.is_visible()

    @allure.step("Получение имени текущего пользователя")
    def get_logged_in_username(self):
        return self.username_label.inner_text()
