# numbers=[3,43,56,32,55,76]

# def even(x):

#     return x % 2== 0


# evens=list(filter(even,numbers))

# print("Even Number=> ",evens)


print("Using filter function")


numbers=[3,43,56,32,55,76]


evens=list(filter(lambda x: x % 2== 0,numbers))

print("Even Numbers=> ",evens)