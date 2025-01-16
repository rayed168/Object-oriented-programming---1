class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        print(f"{self.name} is singing a song which is called {song}")

    def dance(self):
        print(f"{self.name} is dancing")    

song = input("Enter a song's name : ")


Sam = Parrot("Sam", 10)

Sam.sing(song)
Sam.dance()