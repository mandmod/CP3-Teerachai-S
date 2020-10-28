class Customer:
    name = ''
    lastName = ''
    age = 0

    def addCart(self):
        print('Added product to ', self.name, self.lastName, 'Cart')


customer1 = Customer()
customer1.name = 'Mr.Teerachai'
customer1.lastName = 'S'
customer1.addCart()

customer2 = Customer()
customer2.name = 'Mr.Modlove'
customer2.lastName = 'S'
customer2.addCart()

customer3 = Customer()
customer3.name = 'Mr.goldhand'
customer3.lastName = 'S'
customer3.addCart()
