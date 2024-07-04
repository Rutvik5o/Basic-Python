import sys

print("Number Of Arguments=> ",len(sys.argv))

print("Argument List=> ",str(sys.argv))


try:
    x=int(sys.argv[1])

    y=int(sys.argv[2])

    z=x/y

    print("Result=> ",z)
    
except IndexError:

    print("Enter two arguments")

except ZeroDivisionError:

    print("Can't Divide by zero")
else:

    print("Thanks for enter two argments")

