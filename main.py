class Animal:
    def __init__(self, name, species, age, enclosure, health="Healthy"):
        self.name = name
        self.species = species
        self.age = age
        self.enclosure = enclosure
        self.health = health

    def interact(self):
        return f"{self.name} the {self.species} is interacting with visitors."

    def feed(self):
        self.health = "Healthy"
        return f"{self.name} has been fed and is now healthy."


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the {animal.enclosure} enclosure.")

    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name.lower() == animal_name.lower():
                self.animals.remove(animal)
                print(f"{animal.name} has been removed from the zoo.")
                return
        print(f"{animal_name} is not in the zoo.")

    def display_animals(self):
        if not self.animals:
            return "No animals in the zoo."
        else:
            animal_list = []
            for animal in self.animals:
                animal_list.append(f"{animal.name} - {animal.species} - Age: {animal.age} - Health: {animal.health}")
            return "\n".join(animal_list)

    def schedule_interaction(self, animal_name, interaction):
        for animal in self.animals:
            if animal.name.lower() == animal_name.lower():
                return animal.interact() if interaction == "interact" else animal.feed()
        return f"{animal_name} is not in the zoo."


def get_animal_info():
    name = input("Enter animal's name: ")
    species = input("Enter animal's species: ")
    age = int(input("Enter animal's age: "))
    enclosure = input("Enter animal's enclosure: ")
    return Animal(name, species, age, enclosure)


def main():
    zoo = Zoo()

    while True:
        print("\nZoo Management System")
        print("1. Add an animal")
        print("2. Remove an animal")
        print("3. Display animals")
        print("4. Schedule interaction")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_animal = get_animal_info()
            zoo.add_animal(new_animal)

        elif choice == "2":
            animal_name = input("Enter the name of the animal to remove: ")
            zoo.remove_animal(animal_name)

        elif choice == "3":
            animals_info = zoo.display_animals()
            print(animals_info)

        elif choice == "4":
            animal_name = input("Enter the name of the animal: ")
            interaction_type = input("Enter the interaction type (interact/feed): ")
            interaction_result = zoo.schedule_interaction(animal_name, interaction_type)
            print(interaction_result)

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
