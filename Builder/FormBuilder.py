class FormBuilder:
    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.address = None
        self.district = None
        self.city = None
        self.birth_date = None

    def set_address(self, address):
        self.address = address

    def set_district(self, district):
        self.district = district

    def set_city(self, city):
        self.city = city

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date
