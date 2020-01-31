from model.contact import Contact


def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Stachu", middlename="Jezyna", lastname="Kowal"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
