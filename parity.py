# x = int(input("What is x? "))

# if x % 2 == 0:
#     print("x is even")
# else:
#     print("x id odd")


# Using main and function

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

    # other method 1
    # return True if n % 2 ==0 else False  # Pythonic

    # other method 2
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    
main()
    