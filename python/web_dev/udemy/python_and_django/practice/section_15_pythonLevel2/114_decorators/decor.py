# s = "GLOBAL VARIABLE!"
#
# def func():
#     mylocal = 10
#     print(locals())
#     print(globals())
#
# func()
# print(s)

# def hello(name = "Jose"):
#     return "hello "+name
#
# print(hello())
#
# ##sets equal to function
# ##
# mynewgreet = hello
#
# print(mynewgreet())

# def hello(name = "Jose"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME"
#
#     ##returns function itself
#     ##
#     if name == "Jose":
#         return greet
#     else:
#         return welcome
#
# x = hello()
# print(x())

# ##pass in functions
# ##
# def hello():
#     return("Hi JOSE!")
#
# def other(func):
#     print("HELLO")
#     print(func)
#
# ##passing function itself
# ##
# other(hello)

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")


## func_needs_decorator = new_decorator(func_needs_decorator)
##quicker way to do above commented out
##
##@new_decorator

func_needs_decorator()
