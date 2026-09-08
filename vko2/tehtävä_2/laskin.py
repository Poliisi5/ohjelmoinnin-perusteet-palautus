operations = {
    1: "+",
    2: "-",
    3: "/",
    4: "*",
    5: "**",
    6: "%",
}

def calc(operation, n1, n2):
    oper = operations[operation]
    expression = f"{n1} {oper} {n2}"
    print(expression)
    print(eval(expression))


def main():
    print("""This is a simple calculator that can do any basic math operation
Supported math operations
1. +
2. -
3. /
4. *
5. **
6. %""")
    operation = int(input("Please type number of the operation you want to execute: "))
    n1 = input("Input the first number you want to use: ")
    n2 = input("Input the second number you want to use: ")
    calc(operation, n1, n2)

main()