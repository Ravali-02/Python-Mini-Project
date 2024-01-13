class justnotcoolerror(Exception):
    pass


x = 2

try:
    # print(x / 0)
    raise Exception("this is just isn't cool, Women.")
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError meaning something is probably undefined..")
except ZeroDivisionError:
    print("Please do not divide by Zero...")
except Exception as error:
    print(error)
else:
    print("No Errors!")
finally:
    print("I'm going to print with or without error.")
