import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle the user's choice
def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Light blue background

# Add a label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
label.pack(pady=20)

# Add buttons for user choices
rock_button = tk.Button(root, text="Rock", font=("Arial", 14), bg="#ff6666", fg="white", activebackground="#ff4d4d", command=lambda: play("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("Arial", 14), bg="#66b3ff", fg="white", activebackground="#3399ff", command=lambda: play("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), bg="#85e085", fg="white", activebackground="#5cd65c", command=lambda: play("scissors"))
scissors_button.pack(pady=10)

# Run the application
root.mainloop()