from random import choice

capital = "Delhi"

bird = "Peacock"

flower = "Rose"

song = "happy birthday"

def randomfunfact():
    funfacts = [
       "kansas is considered flat, but it does have a mountain.",
       "Wichita is the largest city in the state, but many would"
        "guess that it is kansas city.",
       "A cosiderable portion of kansas city is actually in missouri.",
       "Most kansans are annoyed by wizard of Oz references from"
       "people outside of kansas."
    ]

    index = choice("0123")
    print(funfacts[int(index)])

    # if __name__ == "__main__":
randomfunfact()
       



    