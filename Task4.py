import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = get_winner(user_choice, computer_choice)
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Your score: {user_score}  |  Computer's score: {computer_score}")
    
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: -")
    computer_choice_label.config(text="Computer's choice: -")
    result_label.config(text="Result: -")
    score_label.config(text=f"Your score: {user_score}  |  Computer's score: {computer_score}")


root = tk.Tk()
root.title("Rock-Paper-Scissors")

user_score = 0
computer_score = 0

title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your choice: -", font=("Arial", 14))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's choice: -", font=("Arial", 14))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result: -", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your score: 0  |  Computer's score: 0", font=("Arial", 14))
score_label.pack(pady=5)

rock_button = tk.Button(root, text="Rock", width=20, height=2, font=("Arial", 12), command=lambda: play("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, height=2, font=("Arial", 12), command=lambda: play("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, font=("Arial", 12), command=lambda: play("scissors"))
scissors_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", width=20, height=2, font=("Arial", 12), command=reset_game)
reset_button.pack(pady=20)

root.mainloop()
