from tkinter import*
import random

#----------------------------------------------------------------------------------------------
def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            buttons[row][column].config(fg="blue" if player == "X" else "purple")


            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:

            buttons[row][column]["text"] = player
            buttons[row][column].config(fg="blue" if player == "X" else "purple")

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!") 

#----------------------------------------------------------------------------------------------
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="SeaGreen1")
            buttons[row][1].config(bg="SeaGreen1")
            buttons[row][2].config(bg="SeaGreen1")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="SeaGreen1")
            buttons[1][column].config(bg="SeaGreen1")
            buttons[2][column].config(bg="SeaGreen1")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="SeaGreen1")
        buttons[1][1].config(bg="SeaGreen1")
        buttons[2][2].config(bg="SeaGreen1")
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="SeaGreen1")
        buttons[1][1].config(bg="SeaGreen1")
        buttons[2][0].config(bg="SeaGreen1")
        return True
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")

        return "Tie"
    else:
        return False

#----------------------------------------------------------------------------------------------
def empty_spaces():

    spaces = 0

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
#----------------------------------------------------------------------------------------------
def new_game():
    
    global player 

    player = random.choice(players)

    label.config(text= player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
            #buttons[row][column].config(state=NORMAL)

#----------------------------------------------------------------------------------------------
window = Tk()
window.title("Tic Tac Toe")
window.configure(bg="#ADD8E6")  # Light blue background 


players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#label = Label(text= player + " turn", font=("Arial", 40))
#label.pack(side="top")

# Player turn label with padding below
label = Label(text=player + " turn", font=("Arial", 40), bg="#ADD8E6")
label.pack(side="top", pady=20)

#reset_button = Button(text="restart", font=("Arial", 20), command=new_game)
#reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial", 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
        buttons[row][column].config(command=lambda row=row, column=column: next_turn(row, column))

reset_button = Button(text="Restart", font=("Arial", 20), command=new_game, bg="white", fg="black")
reset_button.pack(pady=30)


window.mainloop()