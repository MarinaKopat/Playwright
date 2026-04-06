class AdminPage:
    def __init__(self, page):
        self.page = page
        self.header = page.get_by_role("heading", name="Панель управления")

    def open(self, url):
        self.page.goto(url)
