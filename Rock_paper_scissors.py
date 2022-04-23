import random

def name_to_number(name):
    rspls={"Rock":0,"Spock":1,"Paper":2,"Lizard":3,"Scissors":4}
    return rspls[name]
   

def number_to_name(number):
    rspls={0:"Rock",1:"Spock",2:"Paper",3:"Lizard",4:"Scissors"}
    return rspls[number]
       
   
def play_again():
    """Asks the user if they want to play the game again"""
    while True:
        choose=input("Do you want to play again? Type Yes or No: ")
        user_chooses = choose[0].upper()+choose[1:].lower()
        if user_chooses =="Yes":
            rps()
            break
        elif user_chooses =="No":
            break
        else:
            print("That is not the answer I was looking for. Type 'Yes' or 'No' please :) ")


def rps():
    while True:
        try:
            round_option=int(input("How many rounds do you want to play?"))
        except ValueError:
            print("That is not a (whole) number. Try again please.")
            continue
        else:
            break
       
   
    n=0
    while n!=round_option:
        player_choice=input("Choose Rock, Spock, Paper, Lizard, Scissors")
        proper_player_choice = player_choice[0].upper()+player_choice[1:].lower()
        print(f'\nThis is your choice: {proper_player_choice}')
        player_number=name_to_number(proper_player_choice)
        player_number

        comp_number=random.randrange(0,4)
        comp_choice=number_to_name(comp_number)
        print(f"This is the computer's choice: {comp_choice}")

        decision_factor=(comp_number-player_number)%5
        if decision_factor==2 or decision_factor==1:
            print("Computer wins!")
        elif decision_factor==0:
            print("Tie! I guess like minds do think alike.")
        else:
            print("Player wins! Hooray")
        n+=1
       
    play_again()

#rps()