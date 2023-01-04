#Program to find the Cube of elements up to a given number in python.
#create a function
def cube(n):
    cubes={}
    for i in range(1,n+1):  # use for loop
        cubes[i]=i**3
    return cubes
x=int(input("Enter the number : ")) # x is any variable that takes input from user
print(cube(x))
