from faker import Faker
import random

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")
    
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    
    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        
        if contact_type == "business":
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contacts.append(BusinessContact(first_name, last_name, phone, email, position, company, business_phone))
        else:
            contacts.append(BaseContact(first_name, last_name, phone, email))
    
    return contacts

# Przykładowe użycie
contacts = create_contacts("business", 3)
for contact in contacts:
    contact.contact()
    print("Długość etykiety:", contact.label_length)
