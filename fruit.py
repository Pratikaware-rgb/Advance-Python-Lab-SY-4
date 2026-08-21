#Create a FruitFactory that returns Apple, Mango, or Orange objects Using Factory Pattern . Each fruit class should display its name.
# Product Classes

class Apple:
    def display(self):
        print("Apple Selected")


class Mango:
    def display(self):
        print("Mango Selected")


class Orange:
    def display(self):
        print("Orange Selected")


# Factory Class
class FruitFactory:

    def getFruit(self, choice):

        if choice == 1:
            return Apple()

        elif choice == 2:
            return Mango()

        elif choice == 3:
            return Orange()


# Main Program

factory = FruitFactory()

print("1. Apple")
print("2. Mango")
print("3. Orange")

choice = int(input("Enter your choice: "))

fruit = factory.getFruit(choice)

fruit.display()
