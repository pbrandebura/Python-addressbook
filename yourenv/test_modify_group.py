from model.contact import Contact


def test_modify_first_group(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_group()
    app.session.logout()
