import allure
from .base_page import BasePage


class DashboardPage(BasePage):
    BOARDS_COUNT = '[data-qa="dashboard-stat-total-boards-value"]'
    TOTAL_TASKS_COUNT = '[data-qa="dashboard-stat-total-tasks-value"]'
    CREATE_BOARD_BTN = "//button"
    USERNAME_LABEL = ".header-username"

    @allure.step("Нажать кнопку создания новой доски")
    def click_create_board(self):
        self.page.click(self.CREATE_BOARD_BTN)

    @allure.step("Получить количество досок")
    def get_boards_count(self):
        return self.page.locator(self.BOARDS_COUNT).inner_text()

    @allure.step("Получение имени текущего пользователя")
    def get_logged_in_username(self):
        return self.page.locator(self.USERNAME_LABEL).inner_text()
