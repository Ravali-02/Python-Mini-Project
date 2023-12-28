
# users = ['Ravali', 'Kumarswamy', 'Vanam']

# data = ['Ravali', 42 , True]

# emptylist = []

# print('Ravali' in emptylist)

# print(users [0])
# print(users[-1])

# print(users.index('Vanam'))
# print(users[0:1])
# print(users[1:])
# print(users[-3:-1])
# print(users[0:2])

# print(len(data))
# users.append('Radha')
# print(users)

# users += ['Sushma']
# print(users)

# users.extend(['Chetan', 'Rutvi'])
# print(users)

# users.extend(data)
# print(users)

# users.insert(0, 'Bob')
# print(users)

# users[2:2] = ['Kumarswamy', 'Radha']
# print(users)

# users[1:3] = ['robert', 'JPJ']
# print(users)

# users.remove('Bob')
# print(users)

# print(users.pop())
# print(users)

# data.clear()
# print(data)

# users[1:2] = ['Ravali']
# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
print(nums)


numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy.sort())
print(mycopy)
print(nums)
mycopy.sort()
print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Ravali', 25, True))

anothertuple = (1,3,5,6)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple

print(one)
print(two)
print(hey)

print(anothertuple.count(2))





















