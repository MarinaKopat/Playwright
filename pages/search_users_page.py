import allure
from playwright.sync_api import Page


class SearchUsers:
    def __init__(self, page: Page):
        self.page = page
        self.ADMIN_LINK = '[data-qa="sidebar-admin-link"]'
        self.SEARCH_INPUT = "input.admin-search-input"
        self.USER_EMAIL_CELLS = "xpath=//div[contains(@class, 'admin-table-container')]//td[2]"

    @allure.step("Перейти в раздел административной панели")
    def open_administrative_panel(self):
        self.page.click(self.ADMIN_LINK)

    @allure.step("Поиск пользователя по фразе: {query}")
    def search_user(self, query):
        self.page.fill(self.SEARCH_INPUT, query)

    def get_user_row(self, email: str):
        return self.page.locator(self.USER_EMAIL_CELLS).filter(has_text=email)
