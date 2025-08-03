from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class EducationPage(BasePage):
    """Education programs page class for Ломоносовская гимназия"""

    def __init__(self, driver):
        self.base_url = 'https://ломоносовскаягимназия.рф/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.education_programs = WebElement(driver, '.education-programs, .programs, .curriculum')
        self.humanities_profile = WebElement(driver, '.humanities, .гуманитарный, [href*="гуманитарный"]')
        self.natural_sciences_profile = WebElement(driver, '.natural-sciences, .естественнонаучный, [href*="естественнонаучный"]')
        self.technology_profile = WebElement(driver, '.technology, .технологический, [href*="технологический"]')
        self.enrollment_info = WebElement(driver, '.enrollment, .прием, .admission')
        self.grade_levels = WebElement(driver, '.grade-levels, .классы, .levels')
        self.foreign_languages = WebElement(driver, '.foreign-languages, .иностранные-языки, .languages')
        self.extracurricular = WebElement(driver, '.extracurricular, .внеурочная, .activities')
        self.teachers_info = WebElement(driver, '.teachers, .педагоги, .staff')
        self.schedule_info = WebElement(driver, '.schedule, .расписание, .timetable')

    def get_available_programs(self):
        """Get information about available educational programs"""
        try:
            return self.education_programs.get_text()
        except NoSuchElementException:
            return ""

    def navigate_to_humanities_profile(self):
        """Navigate to humanities profile information"""
        try:
            self.humanities_profile.click()
            return True
        except NoSuchElementException:
            return False

    def navigate_to_natural_sciences_profile(self):
        """Navigate to natural sciences profile information"""
        try:
            self.natural_sciences_profile.click()
            return True
        except NoSuchElementException:
            return False

    def navigate_to_technology_profile(self):
        """Navigate to technology profile information"""
        try:
            self.technology_profile.click()
            return True
        except NoSuchElementException:
            return False

    def get_enrollment_information(self):
        """Get enrollment and admission information"""
        try:
            return self.enrollment_info.get_text()
        except NoSuchElementException:
            return ""

    def get_grade_levels_info(self):
        """Get information about different grade levels"""
        try:
            return self.grade_levels.get_text()
        except NoSuchElementException:
            return ""

    def get_foreign_languages_info(self):
        """Get information about foreign language programs"""
        try:
            return self.foreign_languages.get_text()
        except NoSuchElementException:
            return ""

    def get_extracurricular_activities(self):
        """Get information about extracurricular activities"""
        try:
            return self.extracurricular.get_text()
        except NoSuchElementException:
            return ""

    def get_teachers_information(self):
        """Get information about teaching staff"""
        try:
            return self.teachers_info.get_text()
        except NoSuchElementException:
            return ""

    def get_schedule_information(self):
        """Get schedule and timetable information"""
        try:
            return self.schedule_info.get_text()
        except NoSuchElementException:
            return ""

    def check_program_availability(self, program_name):
        """Check if specific program information is available"""
        try:
            if "гуманитарный" in program_name.lower():
                return self.humanities_profile.is_displayed()
            elif "естественнонаучный" in program_name.lower():
                return self.natural_sciences_profile.is_displayed()
            elif "технологический" in program_name.lower():
                return self.technology_profile.is_displayed()
            else:
                return False
        except NoSuchElementException:
            return False

    def search_education_content(self, search_term):
        """Search within education content"""
        try:
            # Implementation would depend on actual search functionality
            return True
        except NoSuchElementException:
            return False 