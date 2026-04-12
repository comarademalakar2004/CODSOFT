import tkinter as tk
import random

# -------------------------------
# Global Variables (Scores)
# -------------------------------
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

# -------------------------------
# Function: Get computer choice
# -------------------------------
def get_computer_choice():
    return random.choice(choices)

# -------------------------------
# Function: Determine winner
# -------------------------------
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "🤝 It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "🎉 You Win!"
    else:
        return "😢 You Lose!"

# -------------------------------
# Function: Update score
# -------------------------------
def update_score(result):
    global user_score, computer_score
    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1

# -------------------------------
# Function: Play Game
# -------------------------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    update_score(result)

    score_text = f"SCORE → YOU: {user_score} | COMPUTER: {computer_score}"

    computer_output.config(text=computer_choice)

    if "Win" in result:
        result_output.config(text=result, fg="green")
    elif "Tie" in result:
        result_output.config(text=result, fg="orange")
    else:
        result_output.config(text=result, fg="red")

    score_output.config(text=score_text)

# -------------------------------
# Function: Reset Score
# -------------------------------
def reset_score():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    computer_output.config(text="-")
    result_output.config(text="Scores have been reset!", fg="black")
    score_output.config(text="SCORE → YOU: 0 | COMPUTER: 0")

# -------------------------------
# Tkinter UI
# -------------------------------
root = tk.Tk()

# 🪟 Title bar (simulated bold using uppercase)
root.title("ROCK-PAPER-SCISSORS GAME")

root.geometry("400x420")
root.resizable(False, False)

# Theme
bg = "#ffffff"
text = "#000000"

root.configure(bg=bg)

# 🔙 Title back to center
tk.Label(root, text="🎮 Rock-Paper-Scissors Game",
         font=("Arial", 16, "bold"),
         bg=bg, fg="black").pack(pady=15)

tk.Label(root, text="Choose your move:",
         font=("Arial", 12),
         bg=bg, fg=text).pack()

# -------------------------------
# User Input
# -------------------------------
user_input = tk.StringVar(value="rock")

radio_frame = tk.Frame(root, bg=bg)
radio_frame.pack(pady=10)

for choice in choices:
    tk.Radiobutton(radio_frame,
                   text=choice.capitalize(),
                   variable=user_input,
                   value=choice,
                   bg=bg, fg=text,
                   activebackground=bg).pack(side="left", padx=5)

# Buttons
tk.Button(root, text="Play",
          bg="green", fg="white",
          command=lambda: play(user_input.get())).pack(pady=5)

tk.Button(root, text="Reset Score",
          bg="yellow", fg="black",
          command=reset_score).pack(pady=5)

# Computer Choice
tk.Label(root, text="Computer Choice:",
         font=("Arial", 12, "bold"),
         bg=bg, fg="black").pack()

computer_output = tk.Label(root, text="-",
                           font=("Arial", 12),
                           bg=bg, fg=text)
computer_output.pack(pady=5)

# Result
result_output = tk.Label(root, text="",
                         font=("Arial", 14, "bold"),
                         bg=bg)
result_output.pack(pady=10)

# 🔢 Score (BOLD)
score_output = tk.Label(root,
                        text="SCORE → YOU: 0 | COMPUTER: 0",
                        font=("Arial", 12, "bold"),
                        bg=bg, fg=text)
score_output.pack(pady=10)

# Run
if __name__ == "__main__":
    root.mainloop()