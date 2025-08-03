from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class ContactsPage(BasePage):
    """Contact information page class for Ломоносовская гимназия"""

    def __init__(self, driver):
        self.base_url = 'https://ломоносовскаягимназия.рф/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.contact_info = WebElement(driver, '.contact-info, .contacts, .contact-details')
        self.address = WebElement(driver, '.address, .адрес, [class*="address"]')
        self.phone = WebElement(driver, '.phone, .телефон, [class*="phone"]')
        self.email = WebElement(driver, '.email, .почта, [class*="email"]')
        self.contact_form = WebElement(driver, '.contact-form, .form, .feedback-form')
        self.map_location = WebElement(driver, '.map, .location-map, iframe[src*="map"]')
        self.working_hours = WebElement(driver, '.working-hours, .часы-работы, .schedule')
        self.director_info = WebElement(driver, '.director, .директор, .principal')
        self.department_contacts = WebElement(driver, '.department-contacts, .отделы, .departments')
        self.social_media = WebElement(driver, '.social-media, .социальные-сети, .social')
        self.feedback_button = WebElement(driver, '.feedback, .обратная-связь, .contact-us')

    def get_contact_information(self):
        """Get general contact information"""
        try:
            return self.contact_info.get_text()
        except NoSuchElementException:
            return ""

    def get_address(self):
        """Get the school address"""
        try:
            return self.address.get_text()
        except NoSuchElementException:
            return ""

    def get_phone_number(self):
        """Get the school phone number"""
        try:
            return self.phone.get_text()
        except NoSuchElementException:
            return ""

    def get_email_address(self):
        """Get the school email address"""
        try:
            return self.email.get_text()
        except NoSuchElementException:
            return ""

    def check_map_availability(self):
        """Check if map/location is available"""
        try:
            return self.map_location.is_displayed()
        except NoSuchElementException:
            return False

    def get_working_hours(self):
        """Get working hours information"""
        try:
            return self.working_hours.get_text()
        except NoSuchElementException:
            return ""

    def get_director_information(self):
        """Get information about the school director"""
        try:
            return self.director_info.get_text()
        except NoSuchElementException:
            return ""

    def get_department_contacts(self):
        """Get contacts for different departments"""
        try:
            return self.department_contacts.get_text()
        except NoSuchElementException:
            return ""

    def check_social_media_links(self):
        """Check if social media links are available"""
        try:
            return self.social_media.is_displayed()
        except NoSuchElementException:
            return False

    def open_contact_form(self):
        """Open or navigate to contact form"""
        try:
            self.contact_form.click()
            return True
        except NoSuchElementException:
            return False

    def open_feedback_form(self):
        """Open feedback form"""
        try:
            self.feedback_button.click()
            return True
        except NoSuchElementException:
            return False

    def submit_contact_form(self, name, email, message):
        """Submit contact form with provided information"""
        try:
            # Implementation would depend on actual form structure
            # This is a placeholder for form submission logic
            return True
        except NoSuchElementException:
            return False

    def check_contact_form_availability(self):
        """Check if contact form is available"""
        try:
            return self.contact_form.is_displayed()
        except NoSuchElementException:
            return False

    def get_full_contact_details(self):
        """Get all available contact details"""
        contact_details = {
            'address': self.get_address(),
            'phone': self.get_phone_number(),
            'email': self.get_email_address(),
            'working_hours': self.get_working_hours(),
            'director': self.get_director_information()
        }
        return contact_details 