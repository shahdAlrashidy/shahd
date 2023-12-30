class Customer:
     def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")

cust1 = Customer("Lara de Silva" , 100) 
print(cust1.name) 
print(cust1.balance) 


class Customer2:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        

cust2 = Customer2("Lara de Silva")
print(cust2.balance) 



class Customer3:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

cust3 = Customer3("Lara de Silva") 
print(cust3.balance) 
print(cust3)

c3 = cust3 + 230
print(c3.balance)



class Employee:


	def __init__(self):
		print('Employee created.')

	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj

