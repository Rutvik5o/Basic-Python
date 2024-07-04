a=int(input("Enter First Number->"))
b=int(input("Enter Second Number->"))

try:
    c=a/b
    print("Result=> ",c)

except:
    print("Value can't divide by zero")

else:
    print("There is no exception in try block") 
    # If there is exception in try block then only except block execute, no else is executed & if there is no error in try block then try & else block execture.


