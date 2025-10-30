import random
#function to choose a random word
def choose():
    words=["pyton",'programming','jumble','difficult','science','psychology','encylopidia','great','electronics']
    return random.choice(words)

#function to jumble a random word
def jumble(word):
    jumbled= ''.join(random.sample(word, len(word)))
    return jumbled

def thank(p1name,p2name,pp1,pp2):
    print("\n Thanks for playing.")
    print(f"{p1name}'s score:{pp1}")
    print(f"{p2name}'s score:{pp2}")
    if pp1>pp2:
        print(f"\n {p1name} wins! congragulations.")
    elif pp2>pp1:
        print(f"\n {p2name} wins! congragulations.")
    else:
        print("\n its a tie well played both! ")
#main game function
def play():
    p1name=input("Please enter your name player 1")
    p2name=input("Please enter your name player 2")
    pp1=0
    pp2=0
    turn=0
    while True:
        #computers task
        picked_word=choose()
        #create a question
        qn=jumble(picked_word) #jumble is defined else where
        print(qn)
        #player1's turn
        if turn %2==0:
            print(p1name,",its your turn.")
            ans = input("what's on your mind?")
            if ans == picked_word:
                pp1=pp1+1
                print(p1name,"yes your right your score is",pp1)
            else:
                print("better luck next time the ans is",picked_word)
                c=int(input("press 1 to continue and press 0 to quit"))
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
        #player2's turn
        else:
            print(p2name,",its your turn.")
            ans = input("what's on your mind?")
            if ans == picked_word:
                pp2=pp2+1
                print(p2name,"yes your right your score is",pp2)
            else:
                print("better luck next time the ans is",picked_word)
                c=int(input("press 1 to continue and press 0 to quit"))
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
    #next turn
    turn =+1
play() 
    