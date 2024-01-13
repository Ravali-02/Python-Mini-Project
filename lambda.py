from functools import reduce
def squared(num): return num * num


print(squared(2))


def addTwo(num): return num + 2


print(addTwo(12))
def sum(a, b): return a + b


print(sum(2, 5))
# -------------------


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(4))
print(addTwenty(5))
# it takes one or more functions arguments or returns a function as a result
# ###############

# lambda num: num * num
numbers = [3, 4, 5, 6, 45, 35]

# to find the squared of numbers
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

# lambda num: num % 2 != 0
odd_nums = filter(lambda num: num % 2 != 0, numbers)  # to find the odd number
print(list(odd_nums))

# lambda acc, curr: acc + curr
numbers = [1, 3, 5, 6, 8]
# to find the totoal number of values
total = reduce(lambda acc, curr: acc + curr, numbers)
print((total))

# lambda acc, curr:  acc + len(curr)

username = ["Ravali", "Vanam", "Happy Birthday!"]
char_count = reduce(lambda acc, curr:  acc + len(curr), username, 0)
print(char_count)
