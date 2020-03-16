class Form:
    def __init__(self, form_builder):
        self.name = form_builder.name
        self.password = form_builder.password
        self.email = form_builder.email
        self.phone = form_builder.phone
        self.address = form_builder.address
        self.district = form_builder.district
        self.city = form_builder.city
        self.birth_date = form_builder.birth_date

    def print(self):
        print("Name: {}\n Password: {}\n Email: {}\n Phone: {}\n Address: {}\n District: {}\n City: {}\n Birthdate: {}\n".format(
            self.name, self.password, self.email, self.phone, self.address, self.district, self.city, self.birth_date
        ))
