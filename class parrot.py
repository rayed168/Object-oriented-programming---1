class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Sam = Parrot("Sam", 10)
Bob = Parrot("Bob", 15)          

print(f"The first bird's name is {Sam.name}")
print(f"{Sam.name} is {Sam.age} years old")

print(f"The second bird's name is {Bob.name}")
print(f"{Bob.name} is {Bob.age} years old")