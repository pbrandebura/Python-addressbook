from random import randrange

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Helo"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anddd", lastname="newMiddleName")
    contact.full_name = contact.lastname + " " + contact.firstname
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    old_contacts[index] = contact
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
