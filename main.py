def number_input():
    while True:
        try:
            n = int(input("Enter a number: "))
            return n
        except:
            pass

n1 = number_input()
n2 = number_input()

while True:
    operation = input("Enter the symbol of operation: ")
    if operation in "+-*x/":
        print(f"{n1} {operation} {n2} = ", end="")
    if operation == "+":
        print(n1+n2)
    elif operation == "-":
        print(n1-n2)
    elif operation == "x" or operation == "*":
        print(n1*n2)
    elif operation == "/":
        print(n1/n2)
    else:
        print("Such an operation is beyond the scope of this calculator!")
        continue
    break
