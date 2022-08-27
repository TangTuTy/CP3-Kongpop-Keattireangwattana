class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart (self):
        print("Added to ",self.name,self.lastname,self.age,"yearold cart")

customer1 = Customer()
customer1.name="Kongpop"
customer1.lastname="Keat"
customer1.age="17"
customer1.addCart()

customer2 = Customer()
customer2.name="Tang"
customer2.lastname="T"
customer2.age="18"
customer2.addCart()

customer3 = Customer()
customer3.name="Kong"
customer3.lastname="K"
customer3.age="15"
customer3.addCart()