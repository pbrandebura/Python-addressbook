from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="Anddd", middlename="newMiddleName"))
    app.session.logout()
