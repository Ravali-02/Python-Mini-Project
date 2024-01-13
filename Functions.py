def hello():
    print("Hello World!")
hello() #calling the function

# def sum(num1, num2):
#     print(num1 + num2)

# sum(3, 4)
# sum(1, 3)
# sum(2, 4)
# sum(100, 3)# calling the function with parameters

# def sum(num1, num2):
#     return num1 + num2

# total = sum(2, 30)
# print(total)


def sum(num1=0, num2=0):
   if (type(num1) is not int or type(num2) is not int):
       return 0
   return num1 + num2

total = sum(7, 3)
print(total)

def mulitple_codes(*args):
    print(args)
    print(type(args))
mulitple_codes("ravs", "go", "come")

def mult_codes_lesson(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_codes_lesson(first="ravs", middle="vanam", last="kumar")