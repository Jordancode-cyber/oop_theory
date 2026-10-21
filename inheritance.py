class familymember:
    def __init__(self, eye_colour, home_village):
        self.eye_colour = eye_colour
        self.home_village = home_village

    def descibemember(self):
        self.eye_colour
        self.home_village
        return f"Family eye colour {self.eye_colour} from home village {self.home_village}"

member1 = familymember('brown', 'Arua City')
member2 = familymember('blue', 'Hoima')

print(member1.descibemember())
print(member2.descibemember())

##Inheritance from parent class
class Matthew(familymember):
    def __init__(self, eye_colour, home_village, occupation):
        super().__init__(eye_colour, home_village)
        self.occupation = occupation
    def describemember(self):
        base_description = super().descibemember()
        return f"{base_description} and works as a {self.occupation}"

occupation1 = Matthew('brown', 'Arua City', 'Software Engineer')
print(occupation1.describemember())


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x= Person("John", "Doe")
x.printname

class Student(Person):
    def __init__(self, fname, lname, year):                    # (pass) if not adding any other attributes to the child class
        super().__init__(fname, lname)
        self.graduationyear = year       #overrides parent's __init__ function           
    def welcome(self):
        print(f"Welcome {self.fname}, {self.lname}, to class of, {self.graduationyear}")
x = Student("Mike", "Olsen", 2019)
x.printname
