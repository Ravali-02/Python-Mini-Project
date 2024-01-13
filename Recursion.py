def add_three(num):

    if (num >= 10):
        return num + 1
    
    total = num + 1
    print(total)

    return add_three(total)

# add_three(0)
mynew = add_three(0)

print(mynew)


