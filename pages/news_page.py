from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class NewsPage(BasePage):
    """News and announcements page class for Ломоносовская гимназия"""

    def __init__(self, driver):
        self.base_url = 'https://ломоносовскаягимназия.рф/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.news_container = WebElement(driver, '.news-container, .announcements, .news-list')
        self.news_items = WebElement(driver, '.news-item, .announcement-item, .news-article')
        self.news_title = WebElement(driver, '.news-title, .announcement-title, h2, h3')
        self.news_date = WebElement(driver, '.news-date, .announcement-date, .date')
        self.news_content = WebElement(driver, '.news-content, .announcement-content, .content')
        self.news_filter = WebElement(driver, '.news-filter, .filter, select')
        self.search_news = WebElement(driver, '.search-news, input[placeholder*="поиск"], .search')
        self.pagination = WebElement(driver, '.pagination, .page-numbers, .pager')
        self.back_to_main = WebElement(driver, 'a[href="/"], .back-to-main, .home-link')

    def get_news_count(self):
        """Get the number of news items displayed"""
        try:
            # This would need to be implemented based on actual page structure
            return len(self.driver.find_elements_by_css_selector('.news-item, .announcement-item'))
        except:
            return 0

    def get_latest_news_title(self):
        """Get the title of the latest news item"""
        try:
            return self.news_title.get_text()
        except NoSuchElementException:
            return ""

    def get_latest_news_date(self):
        """Get the date of the latest news item"""
        try:
            return self.news_date.get_text()
        except NoSuchElementException:
            return ""

    def filter_news_by_category(self, category):
        """Filter news by category if filter is available"""
        try:
            self.news_filter.click()
            # Implementation would depend on actual filter structure
            return True
        except NoSuchElementException:
            return False

    def search_news_content(self, search_term):
        """Search within news content"""
        try:
            self.search_news.clear()
            self.search_news.send_keys(search_term)
            return True
        except NoSuchElementException:
            return False

    def navigate_to_news_detail(self):
        """Navigate to the first news item detail page"""
        try:
            self.news_items.click()
            return True
        except NoSuchElementException:
            return False

    def go_back_to_main(self):
        """Navigate back to main page"""
        try:
            self.back_to_main.click()
            return True
        except NoSuchElementException:
            return False

    def check_news_availability(self):
        """Check if news section is available and has content"""
        try:
            return self.news_container.is_displayed()
        except NoSuchElementException:
            return False

    def get_news_content_preview(self):
        """Get a preview of the news content"""
        try:
            return self.news_content.get_text()[:200] + "..."  # First 200 characters
        except NoSuchElementException:
            return "" 