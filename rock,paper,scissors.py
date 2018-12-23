from random import randint
option = ["stone","paper","scissor"]
comp = option[randint(0,2)]
print("Welcome human player to the world of rock, papers and scissors...\nYour options are: 1.stone 2.paper 3.scissor")
human = False
#
while human == False:
    
    human_input = input("What do you choose human? :")
    human = human_input.lower()
    print("Well, the Computer says :" ,comp)
    if comp == human:
        print("Oh!It's a tie! I never knew a human could counter me  :<")
    elif comp == "stone":
        if human == "paper":
            print("You defeated me...NO...Let us play again...How about a drink of spirit?")
        elif human == "scissor":
                print("I knew you people would never make it...I won!!!!")
    elif comp == "paper":
        if human == "stone":
            print("I covered you...")
        elif human == "scissor":
            print("you can't cut me!")
    elif comp=="scissor":
       if human=="paper":
           print("I cut ya!!!!")
       elif human == "stone":
           print("Noooooo....You broke me...")
    human = False
    comp = option[randint(0,2)]
