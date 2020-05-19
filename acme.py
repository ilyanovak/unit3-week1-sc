import random

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        '''
        As an employee of Acme Corporation, you're always looking for ways to better
        organize the vast quantities and variety of goods your company manages and
        sells. Everything Acme sells is considered a `Product`, and must have the 
        following fields (variables that live "inside" the class)
        '''

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        '''
        Calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        '''

        stealable_value = self.price / self.weight
        if stealable_value < 0.5:
            print("Not so stealable...")
        elif stealable_value < 1.0:
            print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        '''
        Calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.", if it is
        greater or equal to 10 but less than 50 return "...boom!", and otherwise
        return "...BABOOM!!"
        '''

        explode_value = self.flammability * self.weight
        if explode_value < 10:
            print("...fizzle.")
        elif explode_value >= 1.0:
            print("...BABOOM!!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.weight = 10

    def explode(self):
        print("..it's a glove.")

    def punch(self):
        '''
        Returns "That tickles." if the weight is below 5,
        "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, 
        and "OUCH!" otherwise
        '''

        if self.weight < 5:
            print("That tickles.")
        elif (self.weight >= 5) & (self.weight < 15):
            print("Hey that hurt!")
        else:
            print("OUCH!")