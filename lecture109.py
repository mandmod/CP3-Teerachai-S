class Animal():
    def eat(self):
        print('Eating Eating !')


class Cat(Animal):
    __name = ''

    def setName(self, text):
        self.name = text
        print('Setting New Cat Name = ', self.name)

    def eat(self):
        print('Meoww !! ', self.name)


cat1 = Cat()
cat1.name = 'TT'
cat1.setName()
cat1.eat()
