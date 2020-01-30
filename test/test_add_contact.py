from model.contact import Contact


def test_test_add_contact(app):
    app.contact.create(Contact(firstname="Stachu", middlename="Jezyna", lastname="Kowal"))


def test_test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname=""))
