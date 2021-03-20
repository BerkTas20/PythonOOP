class Dog: #superclass
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    #polymorphism
    def bark(self):
        return 'Woof!'  

class Kangal(Dog):
    def __init__(self, name, age, friendliness):
        super(). __init__(name, age, friendliness)
   
    def bark(self):
        return 'Arf Arf!'

class Poodle(Dog):
    def __init__(self, name,age, friendliness):
        super(). __init__(name, age, friendliness)      

    def shedding_amount(self):
        return 0

class GoldenRetriever(Dog):
    def __init__(self, name,age, friendliness):
        super(). __init__(name, age, friendliness)   


    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7        


#multiple inheritance
class Bulldog(Poodle, GoldenRetriever): #m.i
    def __init__(self, name,age, friendliness): #m.i
        super(). __init__(name, age, friendliness) #m.i

    def bark(self):
        return 'Auuuuu!'

karabela = Kangal('Karabela', 2, 10)   #m.i
bulldie = Bulldog('Bulldog', 1, 10)
generic_doggo = Dog('Gene', 10, 10)
print(bulldie.bark())
print(karabela.bark())
print(generic_doggo.bark())



# print(bulldie.shedding_amount()) #m.i
# print(bulldie.fetch_ability()) #m.i