def decorators(func):

    def wrapper():

        print("Transaction Started...")

        func()

        print("Transaction Closed")


    return wrapper
    

#first way to execute
# def hello(): #arg of func
#     print("Executing important transaction")

# hello1=decorators(hello)

# hello1()




#second way to execture
@decorators  #hello1 = decorators(hello)  equally 

def hello():
     print("Executing important transaction")

hello()