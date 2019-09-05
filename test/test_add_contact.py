from selenium.webdriver.firefox.webdriver import WebDriver
from model.contact import Contact
import unittest


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def tearDown(self):
        self.wd.quit()

    def test_test_add_contact(self):
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.create_contact(wd, Contact(firstname="Stachu", middlename="Jezyna", lastname="Kowal"))
        self.logout(wd)

    def test_test_add_empty_contact(self):
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.create_contact(wd, Contact(firstname="", middlename="", lastname=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, user, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page(wd)



if __name__ == "__main__":
    unittest.main()
