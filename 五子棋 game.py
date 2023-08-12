from tkinter import *
import random


def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() == False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=player + " turn")

            elif check_winner() is True:
                label.config(text=player + " wins")

            elif check_winner() == "Tie":
                label.config(text=" Tie!")

        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=player + " turn")

            elif check_winner() is True:
                label.config(text=player + " wins")

            elif check_winner() == "Tie":
                label.config(text=" Tie!")


def check_winner():

    for row in range(11):
        for column in range(11):
            if column < 7 and buttons[row][column]['text'] == buttons[row][column+1]['text'] == buttons[row][column+2]['text'] == buttons[row][column+3]['text'] == buttons[row][column+4]['text'] != "":
                buttons[row][column].config(bg='green')
                buttons[row][column+1].config(bg='green')
                buttons[row][column+2].config(bg='green')
                buttons[row][column+3].config(bg='green')
                buttons[row][column+4].config(bg='green')
                return True

            if row < 7 and buttons[row][column]['text'] == buttons[row+1][column]['text'] == buttons[row+2][column]['text'] == buttons[row+3][column]['text'] == buttons[row+4][column]['text'] != "":
                buttons[row][column].config(bg='green')
                buttons[row+1][column].config(bg='green')
                buttons[row+2][column].config(bg='green')
                buttons[row+3][column].config(bg='green')
                buttons[row+4][column].config(bg='green')
                return True

            if row < 7 and column < 7 and buttons[row][column]['text'] == buttons[row+1][column+1]['text'] == buttons[row+2][column+2]['text'] == buttons[row+3][column+3]['text'] == buttons[row+4][column+4]['text'] != "":
                buttons[row][column].config(bg='green')
                buttons[row+1][column+1].config(bg='green')
                buttons[row+2][column+2].config(bg='green')
                buttons[row+3][column+3].config(bg='green')
                buttons[row+4][column+4].config(bg='green')
                return True

            if row < 7 and column > 3 and buttons[row][column]['text'] == buttons[row+1][column-1]['text'] == buttons[row+2][column-2]['text'] == buttons[row+3][column-3]['text'] == buttons[row+4][column-4]['text'] != "":
                buttons[row][column].config(bg='green')
                buttons[row+1][column-1].config(bg='green')
                buttons[row+2][column-2].config(bg='green')
                buttons[row+3][column-3].config(bg='green')
                buttons[row+4][column-4].config(bg='green')
                return True

    if empty_spaces() is False:
        for row in range(11):
            for column in range(11):
                buttons[row][column].config(bg='yellow')
        return "Tie"

    else:
        return False


def empty_spaces():

    for row in range(11):
        for column in range(11):
            if buttons[row][column]["text"] == "":
                return True
    return False


def new_game():

    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(11):
        for column in range(11):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ['x', 'o']
player = random.choice(players)
buttons = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side='top')

reset_button = Button(text='restart', font=('consolas', 20), command=new_game)
reset_button.pack(side='bottom')

frame = Frame(window)
frame.pack()

for row in range(11):
    for column in range(11):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=3, height=1,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
