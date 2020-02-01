from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Helo"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anddd", lastname="newMiddleName")
    contact.full_name = contact.lastname + " " + contact.firstname
    contact.id = old_contacts[0].id
    old_contacts[0] = contact
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
