#Polymorphism is the forms where we have many methods say but they have different forms with same names 

class car():
    def __init__(self):
        pass

    def sound(self):
        print("car sound!")

class bus():
    def __init__(self):
        pass

    def sound(self):
        print("bus sound!")

car1 = car()
bus2 = bus()

car1.sound()
bus2.sound()