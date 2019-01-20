# declare and assign 'My name is' to a new variable called 'myNameIs'
myNameIs = ("My Name Is")
# define a new function with 1 parameter and print myNameIs and the value
# of the function parameter
def function1 ():
    print (myNameIs)
function1 ()
# define a new function with 1 parameter. The function should print the value of the
# parameter under these conditions:
    # if the value equals 5
    # if the value equals 9
    # if the value equals 'Pesho is cool'
    # if the value doesn't equal any of the above print 'Maxata e top!'
    
def function2 (x):
    if x == 5:
        print ("Pesho is cool")
    if x == 9:
        print ("Pesho is not cool")
    if x == 'Pesho is cool':
        print ("Pesho is neutral")
    else:
        print ("Maxata e top!")
function2 ("Pesho is col")

# define a new function with 2 parameters. The function should print the sum of the values
# parameter under these conditions:
    # if the first value is greater than the second
    # if the first value is less than the second and greater than 0
    # if the value doesn't conform to any of the above print x, y and z concatenated with '*' inbetween


def samocska(x,y,z):
    if x > y:
        print (x + y)
    if y > x > 0:
        print (x + y)
    else:
        print(str(x) + '*' + str(y) + '*' + str(z))
samocska(0,2,3)
# 3
print ("(\__/)")
print ("(='.'=)")
print ("(\")_(\")")
# string quote escape with "\".

def kzl(a,b,c,d,e,f):
    if a > b + c + d + e + f:
        print ("(\__/)")
        print ("(='.'=)")
        print ("(\")_(\")")
        samocska(3,18,6)
kzl(38,2,3,5,8,4)
