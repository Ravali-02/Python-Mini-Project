# closure is a function having access to th scope of its parent
# fucntion after the parent funtion has returned
# global is use out of parent function
# # nonlocal is use within the parent functions of another function

# def parent_fu(person):
#     coins = 3

#     def play_G():
#         nonlocal coins
#         coins -=1
#         if coins > 1:
#            print("\n" + person + " Has " + str(coins) + " coins left.\n")
#         elif coins == 1:
#             print("\n" + person + " Has " + str(coins) + " coins left.\n")
#         else:
#             print("\n" + person + " is out of coins left.\n")

#     return play_G
# ravs = parent_fu("ravs")
# chetu = parent_fu("chetu")
# ravs()
# chetu()
# ravs()
# chetu()
# chetu()

x = 'a'

if (x != 'a'):

    print("This is not a.")


else:
    print("This is a.")
