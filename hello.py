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

# create a function to identify the common elements in two list and return as list

def common_element(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))

test = common_element([1,2,3,4,5,6,7], [3,5,8,9])
print(test)


