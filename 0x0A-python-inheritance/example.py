#!/usr/bin/python3
"""Representation of Contact class"""


class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name"""
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):

    def order(self, order):
        print("If this were a real system we would send "
              "{} order to {}".format(order, self.name))


class Friends(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.email}, {self.phone}"


c1 = Contact("Bayo", "bayo@example.net")
s1 = Supplier("Tayo", "tayo@example.net")
f1 = Friends("Ayo", "ayo@example.net", "+234819293939")

print(c1)
print(s1)
print(f1)
# print(f1.name)
