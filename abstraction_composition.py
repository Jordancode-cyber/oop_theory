##What a class must do -- abstraction##
class Robot:
    def make_popcorn(self):
        self._heat_pan()
        self._add_oil()
        self._add_corn()
        self._pop_the_corn()
        print("Popcorn is ready")

    def _heat_pan(self):
        print("Heating the pan")

    def _add_oil(self):
        print("Add oil to heated pan")

    def _add_corn(self):
        print("Adding corn")

    def _pop_the_corn(self):
        print("Popping")

robot = Robot()

robot.make_popcorn()

#Composition -designed principle where a complex class is built 
#by adding simple independent classes
#The class has the attributes
class Tail:
    def wag(self):
        print("Wag wag")

class Dog:
    def __init__(self, name):
        self.name = name
        self.tail = Tail()

    def greet(self):
        print("Woof woof, happy to see you")
        self.tail.wag

##Combined example##
class Speaker:
    def play_music(self):
        print("Boom am playing music")

class DancingRobot:
    def __init__(self):
        self.speaker = Speaker()

    def dance(self):
        self.speaker.play_music()
        print("Kutama")
        print("Saka")
        print("Martinelli")

skl = Speaker()

skl.play_music()
