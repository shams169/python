from pprint import pprint

class Dog:
    # Class Attribute
    species = "Canis Familiaris"
    
    # Class instantiator
    def __init__(self, name, age):
        # These are instance attributes
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} has age {self.age}"

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussel(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


class Service:
    data = []

    def __init__(self, other_data):
        self.other_data = other_data



def main():
    #buddy = Dog("Buddy", 9)
    #miles = Dog("Miles", 10)




    #print(buddy.name, buddy.age)
    # print(buddy.species)
    # print(miles.species)
    #buddy.species = "New One"
    # print(miles.species)
    # print(buddy.species)
    # print(Dog.species)

    #pprint(Dog.__dict__)
    # print(buddy)

    # ser = Service(10)
    # print(ser.data)
    # ser.data.append("val1")
    # print(ser.data)
    # print(Service.data)

    miles = JackRussel("Miles", 4)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 5)

    print(miles.species)
    print(miles.speak("Woof Wood"))
 

main()