import turtle 
turtle.speed(2)
turtle.shape('turtle')

# basic function
def add(n1,n2):
    return n1+n2

n = 10
m = 5
result = add(n,m)
print(result)

number1 = 10
number2 = 20
print(add(number1,number2))
print(add(20,10))

def drawSquare(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.exitonclick() 

drawSquare(200)
# drawSquare(100)