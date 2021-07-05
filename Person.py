  
class Person:
    def __init__(self, city, address, phone_number):
        self._city = city
        self._address = address
        self._phone_number = phone_number

#muistiinpanosdfgh wertyu er
#ghjklugfghj fghigj

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value



    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        #muokkailua spotwepotuwpoeti
        return f'City: {self._city}\nPhone: {self._phone_number}'