from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import pymysql


def reset_button():
    f4 = Frame()
    f4.place(x=135, y=100, width=328, height=370)
    f4.config(bg="red")
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b1))
    b2 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b2))
    b3 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b3))
    b4 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b4))
    b5 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b5))
    b6 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b6))
    b7 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b7))
    b8 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b8))
    b9 = Button(f4, text=' ', font=('colonos', 20), height=3,
                width=6, bg="#2c3339", command=lambda: check(b9))
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1, padx=5)
    b3.grid(row=2, column=2)
    b4.grid(row=3, column=0, pady=5)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)


def build_buttons():

    f3 = Frame()
    f3.config(bg="#3e4448")
    f3.place(x=0, y=0, width=600, height=600)
    label_playarea1 = Label(f3, bg="#2c3339", fg="red",
                            textvariable=player1, font=('colonos', 15))
    label_playscore = Label(f3, bg="#2c3339", fg="red",
                            text=p1_score, font=('colonos', 15))

    label_playarea1.grid(row=0, column=0, padx=10, pady=10)
    label_playscore.grid(row=0, column=1, padx=10, pady=10)

    label_playarea2 = Label(f3, bg="#2c3339", fg="yellow",
                            textvariable=player2, font=('colonos', 15))
    label_playscore2 = Label(
        f3, bg="#2c3339", fg="yellow", text=p2_score, font=('colonos', 15))

    label_playarea2.grid(row=1, column=0, padx=10, pady=10)
    label_playscore2.grid(row=1, column=1, padx=10, pady=10)
    reset_button()
    reset_but = Button(f3, bg="#2c3339", fg="white", text='Reset', height=2,
                       width=10, command=build_buttons)
    reset_but.place(x=125, y=500)
    exit = Button(f3, bg="#2c3339", fg="white", text='Exit', height=2,
                  width=10, command=root.destroy)
    exit.place(x=375, y=500)


def ask_me(ask):
    if(ask == True):
        disable_button()
    else:
        database_insert()
        database_display()
        messagebox.showinfo('Tictactoe', 'Game Score Saved')
        root.destroy()


def check_winner():
    global winner
    global p1_score
    global p2_score
    winner = False
    if(b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
        b1.config(bg="grey", fg="red")
        b2.config(bg="grey", fg="red")
        b3.config(bg="grey", fg="red")
        winner = True
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        p1_score += 1
        disable_button()
    elif(b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
        b4.config(bg="grey", fg="red")
        b5.config(bg="grey", fg="red")
        b6.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
        b7.config(bg="grey", fg="red")
        b8.config(bg="grey", fg="red")
        b9.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
        b1.config(bg="grey", fg="red")
        b4.config(bg="grey", fg="red")
        b7.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
        b2.config(bg="grey", fg="red")
        b5.config(bg="grey", fg="red")
        b8.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        b3.config(bg="grey", fg="red")
        b6.config(bg="grey", fg="red")
        b9.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
        b1.config(bg="grey", fg="red")
        b5.config(bg="grey", fg="red")
        b9.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        b3.config(bg="grey", fg="red")
        b5.config(bg="grey", fg="red")
        b7.config(bg="grey", fg="red")
        winner = True
        p1_score += 1
        ask = messagebox.askyesno("tic tac toe", "X wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O'):
        b1.config(bg="grey", fg="yellow")
        b2.config(bg="grey", fg="yellow")
        b3.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O'):
        b4.config(bg="grey", fg="yellow")
        b5.config(bg="grey", fg="yellow")
        b6.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O'):
        b7.config(bg="grey", fg="yellow")
        b8.config(bg="grey", fg="yellow")
        b9.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O'):
        b1.config(bg="grey", fg="yellow")
        b4.config(bg="grey", fg="yellow")
        b7.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'):
        b2.config(bg="grey", fg="yellow")
        b5.config(bg="grey", fg="yellow")
        b8.config(bg="grey", fg="yellow")
        winner = True
        p2_score += 1
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        b3.config(bg="grey", fg="yellow")
        b6.config(bg="grey", fg="yellow")
        b9.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'):
        b1.config(bg="grey", fg="yellow")
        b5.config(bg="grey", fg="yellow")
        b9.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):
        b3.config(bg="grey", fg="yellow")
        b5.config(bg="grey", fg="yellow")
        b7.config(bg="grey", fg="yellow")
        p2_score += 1
        winner = True
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()
    elif(b1['text'] != ' ' and b2['text'] != ' ' and b3['text'] != ' ' and b4['text'] != ' ' and b5['text'] != ' ' and b6['text'] != ' ' and b7['text'] != ' ' and b8['text'] != ' ' and b9['text'] != ' '):
        b1.config(bg="grey")
        b2.config(bg="grey")
        b3.config(bg="grey")
        b4.config(bg="grey")
        b5.config(bg="grey")
        b6.config(bg="grey")
        b7.config(bg="grey")
        b8.config(bg="grey")
        b9.config(bg="grey")
        ask = messagebox.askyesno("tic tac toe", "O wins")
        ask_me(ask)
        disable_button()


def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def check(b):
    global click
    if(b["text"] == " " and click == True):
        b["text"] = "X"
        click = False
        b.config(fg="red")
        check_winner()
    elif(b["text"] == " " and click == False):
        b["text"] = "O"
        click = True
        b.config(fg="yellow")
        check_winner()
    else:
        messagebox.showerror(
            "tic-tac-toe", " Already been used\n plz select some other box")


def about():
    fabout = Frame()
    fabout.config(bg="#3e4448")
    fabout.place(x=0, y=0, width=600, height=600)
    l1 = Label(fabout, bg="#3e4448", fg="white", text='Creators', font=(
        "colonos", 26, 'underline', 'bold'))
    l1.place(x=240, y=50)
    l1 = Label(fabout, bg="#3e4448", fg="white",
               text='Tirthesh Nahar', font=("colonos", 16))
    l1.place(x=240, y=170)
    l2 = Label(fabout, bg="#3e4448", fg="white",
               text='Samdarshi Tiwari', font=("colonos", 16))
    l2.place(x=240, y=220)
    l3 = Label(fabout, bg="#3e4448", fg="white",
               text='Anand Pandey', font=("colonos", 16))
    l3.place(x=240, y=270)


def login_entry():
    f2 = Frame()
    f2.config(bg="#3e4448")
    f2.place(x=0, y=0, width=600, height=600)
    l1 = Label(f2, bg="#3e4448", fg="white",
               text='Player One', font=("colonos", 16))
    l1.place(x=240, y=100)
    e1 = Entry(f2, bg="#2c3339", fg="white",
               textvariable=player1, font=("colonos", 15))
    e1.place(x=180, y=150)
    l2 = Label(f2, bg="#3e4448", fg="white",
               text='Player Two', font=("colonos", 16))
    l2.place(x=240, y=200)
    e2 = Entry(f2, bg="#2c3339", fg="white",
               textvariable=player2, font=("colonos", 15))
    e2.place(x=180, y=250)
    login_button = Button(f2, bg="#2c3339", fg="white", text='PLAY', width=8,
                          height=2, command=build_buttons)
    login_button.place(x=260, y=300)


def home():
    f1 = Frame()
    f1.config(bg="#3e4448")
    f1.place(x=0, y=0, width=800, height=800)
    intro_label = Label(bg="#3e4448", fg="white", text='Tic - Tac - Toe',
                        font=('colonos', 30, 'bold', 'underline'))
    intro_label.place(x=180, y=6)
    lapic = Label(image=my_img, height=500, width=520, borderwidth=0)
    lapic.place(x=40, y=50)
    play_button = Button(f1, bg="#2c3339", fg="white", font=(10), text='PLAY',
                         command=login_entry, width=8, height=1)
    play_button.place(x=270, y=560)


def database_display():
    conn = pymysql.connect(host="localhost", user="root",
                           passwd="", db="tictactoe")
    c = conn.cursor()
    c.execute("SELECT * FROM hist")
    record = c.fetchall()
    fhist = Frame()
    fhist.config(bg="#3e4448")
    fhist.place(x=0, y=0, width=600, height=600)

    style = ttk.Style()
    style.theme_use("winnative")
    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="silver"

                    )
    style.map('Treeview',
              background=[('selected', 'grey')])
    table = ttk.Treeview(fhist, columns=(0, 1, 2),
                         show="headings", height=30)

    table.pack()
    table.heading(0, text="Matches Played")
    table.heading(1, text="player1 : score")
    table.heading(2, text="player2 : score")

    i = 1

    for row in record:
        table.insert("", 'end',
                     values=("                          "+str(i),
                             "                 " +
                             str(row[0])+"       :        "+str(row[1]),
                             "                 " +
                             str(row[2])+"       :        "+str(row[3])))
        i += 1


def database_insert():
    conn = pymysql.connect(host="localhost", user="root",
                           passwd="", db="tictactoe")
    c = conn.cursor()
    c.execute(
        "INSERT INTO hist(player1,score1,player2,score2) VALUES(%s,%s,%s,%s)", (player1.get(), p1_score, player2.get(), p2_score))
    conn.commit()
    conn.close()


root = Tk()
root.title('Tic-Tac-Toe')
root.geometry("600x600")
menubar = Menu(root)
root.config(menu=menubar)
organize = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Organize", menu=organize)
organize.add_command(label="Home", command=home)
organize.add_command(label="New Game", command=build_buttons)
organize.add_command(label="Edit Name", command=login_entry)
help = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=about)
history = Menu(menubar, tearoff=False)
menubar.add_cascade(label="History", menu=history)
history.add_command(label="History", command=database_display)
player1 = StringVar()
player2 = StringVar()
p1_score = 0
p2_score = 0
click = True
my_img = ImageTk.PhotoImage(Image.open("tic.png").resize((510, 490)))
home()
root.mainloop()
