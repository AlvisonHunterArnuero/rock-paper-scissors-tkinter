import random
import tkinter as tk
from tkinter import messagebox

ply_counter = 0
cpu_counter = 0
main_msg: str = ""


def get_rnd_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def play(ply_choice: str):
    global ply_counter, cpu_counter, main_msg
    cpu_choice = get_rnd_choice()
    if ply_choice == cpu_choice:
        main_msg = "It's a draw!"
        label.config(main_msg)
    elif (ply_choice == "rock" and cpu_choice == "scissors") or (ply_choice == "paper" and cpu_choice == "rock") or (
            ply_choice == "scissors" and cpu_choice == "paper"):
        main_msg = "You Won!"
        ply_counter += 1
    else:
        main_msg = "You Lose!"
        cpu_counter += 1


def show_message_box(title: str, msg: str):
    messagebox.showinfo(title=title, message=msg)


def rps_screen():
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.configure(background="red")
    root.minsize(600, 600)  # width, height
    root.maxsize(600, 600)
    root.geometry("600x600")
    tk.Label(root, text="Rock Paper Scissors", width=10).grid(column=0, row=0)
    tk.Button(root, bg="white", width=10, text="ROCK", command=lambda: play('rock')).grid(column=1, row=0)
    tk.Button(root, width=10, text="PAPER", command=lambda: play('paper')).grid(column=2, row=0)
    tk.Button(root, width=10, text="SCISSORS", command=lambda: play('scissors')).grid(column=3, row=0)
    tk.Button(root, width=10, text="Exit Game", command=root.destroy).grid(column=4, row=0)
    # show_message_box("Info", "Welcome to the RPS Game")
    root.mainloop()


rps_screen()
