class Person:
    #  setup name, address, age, and phone number
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # accessor and mutator methods
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    # display info in a formatted way
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")
        print(f"Phone: {self.__phone}")
        print()

# three instances of the Person class
person1 = Person("John Doe", "123 Maple Street", 23, "815-1234")
person2 = Person("Jane Smith", "456 Oak Avenue", 21, "815-5678")
person3 = Person("Alice Johnson", "789 Pine Road", 27, "815-9012")

# display info for each person
print("Person 1:")
person1.display_info()

print("Person 2:")
person2.display_info()

print("Person 3:")
person3.display_info()
