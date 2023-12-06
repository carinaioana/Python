# Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass 

    def move(self):
        return f"{self.name} is moving."


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth to live young."

    def make_sound(self):
        return "Mammal sound"  


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def make_sound(self):
        return "Bird sound"  


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def lay_eggs_in_water(self):
        return f"{self.name} is laying eggs in the water."

    def make_sound(self):
        return "Fish sound"  


def main():
    lion = Mammal("Arctic Fox", "Tundra", "Golden")
    eagle = Bird("Bald Eagle", "Mountains", 2.5)
    shark = Fish("Shark", "Oceans", "Gray")

    print(lion.move())
    print(lion.give_birth())
    print(lion.make_sound())

    print(eagle.move())
    print(eagle.lay_eggs())
    print(eagle.make_sound())

    print(shark.move())
    print(shark.lay_eggs_in_water())
    print(shark.make_sound())


if __name__ == "__main__":
    main()


