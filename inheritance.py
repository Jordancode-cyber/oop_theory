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