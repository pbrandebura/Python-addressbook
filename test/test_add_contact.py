from model.contact import Contact


def test_test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="Stachu", middlename="Jezyna", lastname="Kowal"))
    app.session.logout()


def test_test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="", middlename="", lastname=""))
    app.session.logout()
