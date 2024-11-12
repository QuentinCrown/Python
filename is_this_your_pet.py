class Pet:
    # Vet name
    vet_name = "Green Valley Veterinary Clinic"
    
    # identification info
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # owner first name
    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    # owner last name
    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    # pet id
    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    # pet name
    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    # pet type
    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # display pet info
    def display_pet_info(self):
        print(f"Owner's Name: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Office: {Pet.vet_name}")
        print()

# real or not
def check_property(pet, property_name):
    if hasattr(pet, property_name):
        print(f"The property '{property_name}' exists in the Pet object.")
    else:
        print(f"The property '{property_name}' does not exist in the Pet object.")

# pets with info assigned
pet1 = Pet("Alice", "Smith", 101, "Buddy")
pet2 = Pet("Bob", "Johnson", 102, "Whiskers", "Cat")
pet3 = Pet("Carol", "Davis", 103, "Goldie", "Fish")

# pet 1
pet1.set_owner_last_name("Brown")
pet1.set_pet_name("Max")

# other info
print("Pet Information:")
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# properties of pets check
print("Property Existence Check:")
check_property(pet1, "_Pet__owner_first_name") 
check_property(pet2, "_owner_first_name")         
check_property(pet3, "_Pet__pet_type")           
