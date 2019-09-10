from model.group import Group


def test_modify_group_name(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(name="sdfsd"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(header="sdf"))
    app.session.logout()