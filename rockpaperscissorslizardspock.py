import random;
def computerChoice():
        random.seed()
        a = random.randint(1,5);
        if(a == 1):
            computer = "rock"
        elif(a == 2):
            computer = "paper"
        elif(a == 3):
            computer = "scissors"
        elif(a == 4):
            computer = "lizard"
        elif(a == 5):
            computer = "spock"
        return computer
b = 1
while(b == 1):
    print("How many times do you wish to play?")
    play = (int)(input())
    for i in range (0, play):
        computerChoice();
        print("type either rock, paper, scissors, lizard, or spock. ")
        user = input()
        if(user.lower() == "rock" and computerChoice().lower() == "rock"):
            print("tie")
        elif(user.lower() == "rock" and computerChoice().lower() == "lizard"):
            print("win")
        elif(user.lower() == "rock" and computerChoice().lower() == "spock"):
            print("lose") 
        elif (user.lower() == "scissors" and computerChoice().lower() == "scissors"):
            print("tie")
        elif(user.lower() == "scissors" and computerChoice().lower() == "spock"):
            print("lose")
        elif(user.lower() == "scissors" and computerChoice().lower() == "lizard"):
            print("win")
        elif (user.lower() == "paper" and computerChoice().lower() == "paper"):
            print("tie")
        elif (user.lower() == "rock" and computerChoice().lower() == "scissors"):
            print("win")
        elif (user.lower() == "scissors" and computerChoice().lower() == "paper"):
            print("win")
        elif (user.lower() == "paper" and computerChoice().lower() == "rock"):
            print("win")
        elif(user.lower() == "paper" and computerChoice().lower() == "spock"):
            print("win")
        elif(user.lower() == "paper" and computerChoice().lower() == "lizard"):
            print("lose")
        elif (user.lower() == "scissors" and computerChoice().lower() == "rock"):
            print("lose")
        elif (user.lower() == "paper" and computerChoice().lower() == "scissors"):
            print("lose")
        elif (user.lower() == "rock" and computerChoice().lower() == "paper"):
            print("lose")
        elif (user.lower() == "lizard" and computerChoice().lower() == "rock"):
            print("lose")
        elif (user.lower() == "lizard" and computerChoice().lower() == "paper"):
            print("win")
        elif (user.lower() == "lizard" and computerChoice().lower() == "scissors"):
            print("lose")
        elif (user.lower() == "lizard" and computerChoice().lower() == "spock"):
            print("win")
        elif (user.lower() == "lizard" and computerChoice().lower() == "lizard"):
            print("tie")
        elif (user.lower() == "spock " and computerChoice().lower() == "scissors"):
            print("win")
        elif (user.lower() == "spock " and computerChoice().lower() == "paper"):
            print("lose")
        elif (user.lower() == "spock " and computerChoice().lower() == "rock"):
            print("win")
        elif (user.lower() == "spock " and computerChoice().lower() == "lizard"):
            print("lose")
        elif (user.lower() == "spock " and computerChoice().lower() == "spock"):
            print("tie")
    print("if you wish to continue type 1 but if not type any other number")
    b = (int)(input())