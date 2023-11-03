# create a function for hello to print
def hello():
    print("Hello world!")

hello()

# create a function to return square of give numeric value
def int_square(n):
    return n**2

num = int_square(int(input("Give integer (1-9):")))

print(f"Squared given integer - {num}")

