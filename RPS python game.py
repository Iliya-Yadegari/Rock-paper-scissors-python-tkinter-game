from random import randint
from tkinter import *

window = Tk()
window.title('Rock Paper Scissors Game')

def Prs():

    t = ["Rock", "Paper", "Scissors"]
    
    computer = t[randint(0,2)]
    
    player = False
    
    while player == False:
    
        player = player_ent.get()    

        if player == computer:
            txt = "Tie!"
        elif player == "Rock":
            if computer == "Paper":
                txt = "You lose!", computer, "covers", player
            else:
                txt = "You win!", player, "smashes", computer
        elif player == "Paper":
            if computer == "Scissors":
                txt = "You lose!", computer, "cut", player
            else:
                txt = "You win!", player, "covers", computer
        elif player == "Scissors":
            if computer == "Rock":
                txt = "You lose...", computer, "smashes", player
            else:
                txt = "You win!", player, "cut", computer
        else:
            txt = "That's not a valid play. Check your spelling!"
    
        res_label = Label(window,text = txt).grid(row = 3, column = 0, padx = 10, pady = 10)
    
    
    
        computer = t[randint(0,2)]
        
main_frm = LabelFrame(window)

player_lbl = Label(main_frm,text = 'Rock, Paper, Scissors?').grid(row = 0, column = 0, padx = 10, pady = 10)
player_ent = Entry(main_frm)
submit_btn = Button(window,text = 'Submit',width = 20, height = 3,command = Prs).grid(row = 1, column = 0, padx = 10, pady = 10)
quit_btn = Button(window,text = 'Exit',width = 20, height = 3, command = window.destroy).grid(row = 2, column = 0, pady = 10, padx = 20)

main_frm.grid(row = 0, column = 0, padx = 10, pady = 10)
player_ent.grid(row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()