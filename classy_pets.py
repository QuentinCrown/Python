# class
class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    # kind
    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    # breed
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    # name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # print details
    def print_details(self):
        print(f"Pet Details:\nKind: {self._kind}\nBreed: {self._breed}\nName: {self._name}")

# Create instances of Pet
pet1 = Pet("Dog", "Golden Retriever", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Polly")

# print for each
pet1.print_details()
print()  
pet2.print_details()
print()  
pet3.print_details()
print()  

# special method
print("__name__: Name of the class:", Pet.__name__)  
print("type(): Class of pet1 object:", type(pet1))   
print("__module__: Module name of Pet class:", Pet.__module__)  
print("__bases__: Base classes of Pet:", Pet.__bases__)         
print("getattr(): Access breed of pet2:", getattr(pet2, "_breed"))  
print("isinstance(): Is pet3 an instance of Pet?", isinstance(pet3, Pet))  
