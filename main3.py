# Functions

# functions are a group of code that preforms a specific task
# whenever you see def it means we're defining a function
# we're creating a function called addtion 
# and always note that a function name should always descibe
# the function is trying to acomplish
def addition():
    answer = 2+2
    print(answer)




    # a function will not run unless you phone it

addition()
# We're creating a function called add
#amd the function receives two parametrs x and y
#parameters are placeholders we use
# to represent the real value we will later put
def add(x,y):
    answer= x + y
    print (answer)

add(500,300)
add(100,50)
add(10,20)
add(80,220)




#create function for addtion subtraction multiplication 
#division, raise to power of,
#all should accept at least 3 parameters
#and call everything






























def addition(a, b, c):
    return a + b + c



def subtraction(a, b, c):
    return a - b - c



def multiplication(a, b, c):
    return a * b * c


def division(a, b, c):
    return a / b / c


def power(a, b, c):
    return a ** b ** c



print("Addition:", addition(10, 5, 2))
print("Subtraction:", subtraction(20, 5, 3))
print("Multiplication:", multiplication(4, 3, 2))
print("Division:", division(100, 5, 2))
print("Power:", power(2, 2, 2))