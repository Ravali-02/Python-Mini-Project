

name = "Ravali"
count = 4

# def happy(username):
#     background_color = "Pink"
#     print(name)
#     print(background_color)
#     print(username)


# happy("vanam")


def differ():
    background_color = "Pink"
    #already diined that count in global variable
    global count
    count += 4 
    print(count)

    def happy(name):
        nonlocal background_color
        background_color = "Purple"
        print(name)
        print(background_color)

    happy("ravali")


differ()

# we can insert another function in function that's called scope
#
