from Rock_paper_scissors import rps

class rps_backend:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    
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
            if user_chooses == "Yes":
                rps()
                break
            elif user_chooses == "No":
                break
            else:
                print("That is not the answer I was looking for. Type 'Yes' or 'No' please :) ")



