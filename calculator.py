first= input("Enter your number:")

operator = input("enter opeartor(+,-,?,*)")

second= input("enter second Number:")

first= int(first)

second= int(second)


if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

else:
     print("invlid operator")

