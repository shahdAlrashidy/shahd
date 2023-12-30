def loop():
    for x in range(10): 
        print (x)
        if x == 3:
            return
        
loop();
####################
print("#"*30)
#pass function as parameter

def twice(y , x):
    return y(y(x))    


def mul(x):
    return x**2   

out = twice(mul , 2)
print(out)

####################
print("#"*30)
#define function inside another

def function1(x):
    def function2(y):
        return y + 2
    return 3 * function2(x)
    
function1(2)
# call the function
# a = function1(2)
# print (a)

# b = function2(2.5) # error
# print (b)

##############################
#global vs local 

x = 1
def add_one (x):
    x = x + 1
    # add one to the local x
    return x


# call the function
y = add_one (x)
print(x)
print(y)


def f1():
    global x
    x = x + 1
    return f"x from f1: {x}"

def f2():
    return f"x from f1: {x+2}"

def f3():
    x = 5
    return f"x from f1: {x+1}" 


x = 0
print(f1()) #global
print(f2()) #global
print(f3()) #local

###############################
print("#"*30)
def func1 (x, a = 1, b = 2 ):
    
    """this function take tree variables. The
    first one have to be supplied, however the
    other two have a default values"""
    return x + a - b


print(help(func1))
print(func1(20))
###############################
print("#"*30)
#assignment using tubles 

t = (1, 2, 3)
x, y, z = t
print (t) # (1, 2,3)
print (y) # 2