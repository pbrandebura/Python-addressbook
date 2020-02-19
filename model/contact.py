from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, full_name=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.full_name = full_name
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.full_name)

    def __eq__(self, other):
        return (self.id == other.id and self.full_name == other.full_name) or self.full_name == other.full_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
