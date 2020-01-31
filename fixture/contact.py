from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("middlename", contact.middlename)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # proceed to edit page
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        contactList = []
        for element in wd.find_elements_by_name("entry"):
            id = wd.find_element_by_name("selected[]").get_attribute('id')
            full_name = element.text
            contactList.append(Contact(id=id, full_name=full_name))
        return contactList
