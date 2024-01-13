
#  F-strings provide a way to embed expressions inside string literals,
#  using a minimal syntax. It should be noted that an f-string is really 
# an expression evaluated at run time, not a constant value. In Python 
# source code, an f-string is a literal string, prefixed with 'f',
# which contains expressions inside braces.

person = "Ravali"
coins = 4

print("\n" + person + " Has " + str(coins) + " coins Left.")

message = "\n%s has %s coins left. " % (person, coins)
print(message)

message = "\n{} has {} coins left. ".format(person, coins)
print(message)

message = "\n{1}  has {0} coins left. ".format(coins, person)
print(message)

message = "\n{person}  has {coins} coins left. ".format(coins=coins, person=person)
print(message)

player = { 'person': 'Ravali', 'coins': 'coins'}

message = "\n{person}  has {coins} coins left. ".format(**player)
print(message)

# ####################
# f-strins this is the way.

message = f"\n{person} has {coins} coins left."
print(message)
message = f"\n{person} has {2 * 5} coins left."
print(message)
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)
message = f"\n{player['person']} has {2 * 5} coins left."
print(message)
message = f"\n{player['coins']} has {2 * 5} coins left."
print(message)
# you can pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")







