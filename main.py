import random
import tkinter as tk
from tkinter import messagebox, StringVar, Tk, IntVar, PhotoImage

root: Tk = tk.Tk()
root.title("Rock Paper Scissors")
root.minsize(500, 200)  # width, height
root.maxsize(500, 200)
root.geometry("500x200")
root.grid_columnconfigure(0, pad=20)
root.grid_columnconfigure(1, pad=20)
root.grid_columnconfigure(2, pad=20)
root.grid_rowconfigure(0, pad=20)
root.grid_rowconfigure(1, pad=20)

for i in range(3):
    root.columnconfigure(i, weight=1)

ply_counter = IntVar()
cpu_counter = IntVar()
main_msg = StringVar()
main_msg.set("Rock, Paper, Scissors")
ply_counter.set(0)
cpu_counter.set(0)

# Load the JPG image
rock_img = PhotoImage(file="rock.gif")
paper_img = PhotoImage(file="paper.gif")
scissors_img = PhotoImage(file="scissors.gif")


def get_rnd_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def play(ply_choice: str):
    global ply_counter, cpu_counter, main_msg
    cpu_choice = get_rnd_choice()
    if ply_choice == cpu_choice:
        main_msg.set(f"It's a draw! {ply_choice.title()} | {cpu_choice.title()}")
    elif (ply_choice == "rock" and cpu_choice == "scissors") or (ply_choice == "paper" and cpu_choice == "rock") or (
            ply_choice == "scissors" and cpu_choice == "paper"):
        main_msg.set(f"You Won! {ply_choice.title()} | {cpu_choice.title()}")
        ply_counter.set(ply_counter.get() + 1)
    else:
        main_msg.set(f"You Lose! {ply_choice.title()} | {cpu_choice.title()}")
        cpu_counter.set(cpu_counter.get() + 1)


def show_message_box(title: str, msg: str):
    messagebox.showinfo(title=title, message=msg)


def rps_screen():
    # Row 0
    tk.Button(root, font=("Arial", 12, "bold"), textvariable=ply_counter).grid(column=0, row=0)
    tk.Button(root, font=("Arial", 12, "bold"), width=25, textvariable=main_msg).grid(column=1, row=0)
    tk.Button(root, font=("Arial", 12, "bold"), textvariable=cpu_counter).grid(column=2, row=0)
    # Row 1
    tk.Button(root,borderwidth=0, image=rock_img, command=lambda: play('rock')).grid(column=0, row=1)
    tk.Button(root, image=paper_img, command=lambda: play('paper')).grid(column=1, row=1)
    tk.Button(root, image=scissors_img, command=lambda: play('scissors')).grid(column=2, row=1)
    # Row 2
    tk.Button(root, padx=10, width=10, text="Exit Game", command=root.destroy).grid(column=1, row=2)
    root.mainloop()


rps_screen()
