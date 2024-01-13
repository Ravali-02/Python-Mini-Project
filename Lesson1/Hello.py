# greeting = 'hello world!'
# print(greeting)
# WTF01= '#######################'
# WTF02= '     @@@@@@@@@@@@      '
# WTF03= '     WHAT THE FcUK      '
# wft2
# print('')
# print(WTF01)
# print(WTF02)
# print(WTF03)
# print(WTF02)
# print(WTF01)

# meaning = 58
# print('')

# if meaning > 28:
#     print('HOP ON!')
# else:
#     print("GET DOWN")


# meaning !=40
# round(meaning)
# print(meaning)

# if meaning > 29:
#     print('true')
# else:
#     print("false")
import math

first = 'Ravali'
last = 'Vanam'
print(type(first))
print(type(first) == tuple)

fullname = first + ' ' + last
print(fullname)

decade = str(1998)
print(type(decade))
print(decade)

statement = " I like the seashore " + decade + "s."
print(statement)
# multiline
multiline = '''
            Hi!    
        How are you?      
    I'm good!

    WHat about you?
    
    Same here.......

'''
print(multiline)

# escaping special characters

statement = 'I\'m good \t what about you \n\nhi!'
print(statement)

# string methods
print(first)
print(first.isupper())
print(first.islower())
print(first.upper())
print(first.lower())
print(first)

print(multiline.title())
print(multiline.replace("good", "great"))
print(multiline)


print(len(multiline))
multiline += "                    "
multiline = "                    " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.rsplit()))
print(len(multiline.lstrip()))

# build a menu
title = "menu".upper()
print(title.center(16, "%"))
print("coffe".ljust(13, ".") + "4$".rjust(3))
print("muffin".ljust(13, ".") + "5$".rjust(3))
print("chessecake".ljust(13, ".") + "6$".rjust(3))

# string index values
# hdd

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
# print(first[0:-2])
print(first[-2])

# string boolen value
print(first.startswith("R"))
print(first.endswith("L"))

# boolean datatype
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, tuple))

# numeric types
price = 100
best_price = int(100)
print(type(price))
print(isinstance(best_price, int))

# float
price = 5.9
best_price = float(5.12)
print(type(price))
print(isinstance(best_price, int))

# comp value
comp_value = 1+5j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# bulit-in function for number
print(abs(price))
print(round(price))
print(round(price, 1))
print(abs(price * -2))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(price))
print(math.floor(price))
# casting a string number
zipcode = "421202"
zip_codevalue = int(421202)
print(isinstance(zip_codevalue, int))

zipcode = "newyork"
print(type(zipcode))


# user types
