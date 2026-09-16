class Car:
    def __init__(self, brand, model, battery=35):
        self.brand = brand
        self.model = model
        self.__battery = battery
        self.__odometer = 0
        self.__passengers = []
    def go(self, distance):
        self.__battery -= distance/20
        self.__odometer += distance
        print("The car traveled",distance,"km")
        print("You have",self.__battery,"wH left")
    def charge(self, wH):
        self.__battery += wH
        print("Car recharged. You now have",self.__battery,"wH")
    def dashboard(self):
        print("Battery:",self.__battery,"wH")
        print("Odometer:",self.__odometer,"KM")
    def enter(self, person):
        if(len(self.__passengers)>=4):
            print("Too many passengers already")
        else:
            self.__passengers.append(person)
            print("Passengers:",end=' ')
            [print(x.name,end=', ') for x in self.__passengers]
            print()

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    def greet():
        print("Hi, I am",self.name)
