# 4 pillars of oop
# inhertiance
# abstraction
# encapsulation


# inhertiance

#users
# - Wizards
# - Archers
# - Orgres 
class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    pass

class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())

# example
class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def _init_(self, name, power):
        self.name = name
        self.power = power

# class Archer(User):
    # print(f'attacking with power of {self.power}')

wizard1 = Wizard()
print(wizard1.sign_in())

# example 

class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def _init_(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name 
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

print(wizard1.sign_in())


