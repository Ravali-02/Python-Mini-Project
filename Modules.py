#  Modules are simply files with the “. py” extension containing Python code that can be imported
#   inside another Python Program. In simple terms, we can consider a module to be the same as
#   a code library or a file that contains a set of functions that you want to include in your application.


from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rps7 import rock_paper_scissiors

print(pi)

# for item in dir(rdm):

#     print(item)


print(kansas.capital)
kansas.randomfunfact()


print(__name__)
print(kansas.__name__)

rock_paper_scissiors()


