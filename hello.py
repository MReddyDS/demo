# create a function for hello to print
# update hello function with input person name

def hello(name):
    print(f"Hello {name}!")

name = input("input your name: ")
hello(name)

# create a function to return square of give numeric value
def int_square(n):
    return n**2

num = int_square(int(input("Give integer (1-9):")))

print(f"Squared given integer - {num}")


