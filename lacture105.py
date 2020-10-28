class Vehicle:
    liceneCode = ''
    serialCode = ''
    face = ''

    def turnOnAirConditioner(self):
        print('Turn on : Air')


class Car(Vehicle):
    def sayHello(self):
        print('Hello World : Car')


class PickUP(Vehicle):
    def sayPickUP(self):
        print('Hello World : PickUP')


class Van(Vehicle):
    def sayVan(self):
        print('Hello World : Van')


car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()
