from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class MainPage(BasePage):
    """Ломоносовская гимназия main page class"""

    def __init__(self, driver):
        self.base_url = 'https://ломоносовскаягимназия.рф/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.school_name = WebElement(driver, 'h1, .school-name, .main-title')
        self.news_section = WebElement(driver, '.news, .announcements, .news-section')
        self.about_section = WebElement(driver, '.about, .school-info, .main-info')
        self.contacts_link = WebElement(driver, 'a[href*="контакты"], a[href*="contacts"]')
        self.education_link = WebElement(driver, 'a[href*="образование"], a[href*="education"]')
        self.news_link = WebElement(driver, 'a[href*="новости"], a[href*="news"]')
        self.menu_toggle = WebElement(driver, '.menu-toggle, .hamburger, .nav-toggle')
        self.main_menu = WebElement(driver, '.main-menu, .navigation, nav')
        self.search_box = WebElement(driver, '.search, input[type="search"], .search-box')
        self.language_switch = WebElement(driver, '.language-switch, .lang-toggle')

    def get_school_name(self):
        """Get the school name from the main page"""
        try:
            return self.school_name.get_text()
        except NoSuchElementException:
            return ""

    def navigate_to_news(self):
        """Navigate to the news section"""
        try:
            self.news_link.click()
            return True
        except NoSuchElementException:
            return False

    def navigate_to_contacts(self):
        """Navigate to the contacts section"""
        try:
            self.contacts_link.click()
            return True
        except NoSuchElementException:
            return False

    def navigate_to_education(self):
        """Navigate to the education section"""
        try:
            self.education_link.click()
            return True
        except NoSuchElementException:
            return False

    def toggle_menu(self):
        """Toggle the mobile menu if present"""
        try:
            self.menu_toggle.click()
            return True
        except NoSuchElementException:
            return False

    def search_content(self, search_term):
        """Search for content on the website"""
        try:
            self.search_box.clear()
            self.search_box.send_keys(search_term)
            return True
        except NoSuchElementException:
            return False

    def get_about_info(self):
        """Get information about the school from the about section"""
        try:
            return self.about_section.get_text()
        except NoSuchElementException:
            return ""

    def check_news_availability(self):
        """Check if news section is available and accessible"""
        try:
            return self.news_section.is_displayed()
        except NoSuchElementException:
            return False

    def switch_language(self):
        """Switch language if language toggle is available"""
        try:
            self.language_switch.click()
            return True
        except NoSuchElementException:
            return False

