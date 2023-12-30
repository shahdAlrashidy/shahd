class A: 
     def setdata(self, value): 
         self.data = value 
     def display(self):
         print(self.data) 
         
         
         
x = A() 
y = A() 


print(x)
print(y)
print(isinstance(x,A))

print("##########################")

x.setdata("Ali") 
y.setdata(3.14159) 
x.display()
y.display()

print("##########################")

x.data = "New value" 
x.display()   #calling the initionated value by name

print("##########################")

x.anothername = "spam" #initionate a new parameter (not clean code)
print(x.anothername)

