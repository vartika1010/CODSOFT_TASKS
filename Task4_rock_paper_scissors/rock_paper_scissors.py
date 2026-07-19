import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.config(bg="#FCE4EC")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0


def play(user_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    player_choice_label.config(text=f"🧑 You: {user_choice}")
    computer_choice_label.config(text=f"💻 Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        result_label.config(fg="#F57C00")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        player_score += 1
        result_label.config(fg="#43A047")
    else:
        result = "😢 Computer Wins!"
        computer_score += 1
        result_label.config(fg="#E53935")

    result_label.config(text=result)

    score_label.config(
        text=f"⭐ Player: {player_score}      Computer: {computer_score}"
    )


def play_again():
    player_choice_label.config(text="🧑 You: -")
    computer_choice_label.config(text="💻 Computer: -")
    result_label.config(text="Choose your move!", fg="#9C27B0")


def reset_score():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    score_label.config(text="⭐ Player: 0      Computer: 0")
    play_again()


title = tk.Label(
    root,
    text="✿ Rock Paper Scissors ✿",
    font=("Helvetica", 24, "bold"),
    bg="#FCE4EC",
    fg="#8E44AD",
)
title.pack(pady=20)

instruction = tk.Label(
    root,
    text="Choose your move!",
    font=("Helvetica", 14),
    bg="#FCE4EC",
    fg="#6A1B9A",
)
instruction.pack()

button_frame = tk.Frame(root, bg="#FCE4EC")
button_frame.pack(pady=25)

button_style = {
    "font": ("Helvetica", 13, "bold"),
    "width": 12,
    "bg": "#D8B4F8",
    "fg": "#4A148C",
    "activebackground": "#C084FC",
    "activeforeground": "white",
    "bd": 0,
    "cursor": "hand2",
    "relief": "flat",
    "pady": 8,
}

rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    command=lambda: play("Rock"),
    **button_style
)
rock_btn.grid(row=0, column=0, padx=8)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    command=lambda: play("Paper"),
    **button_style
)
paper_btn.grid(row=0, column=1, padx=8)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    command=lambda: play("Scissors"),
    **button_style
)
scissors_btn.grid(row=0, column=2, padx=8)

player_choice_label = tk.Label(
    root,
    text="🧑 You: -",
    font=("Helvetica", 15),
    bg="#FCE4EC",
    fg="#6A1B9A",
)
player_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="💻 Computer: -",
    font=("Helvetica", 15),
    bg="#FCE4EC",
    fg="#6A1B9A",
)
computer_choice_label.pack()

result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Helvetica", 18, "bold"),
    bg="#FCE4EC",
    fg="#9C27B0",
)
result_label.pack(pady=20)

score_label = tk.Label(
    root,
    text="⭐ Player: 0      Computer: 0",
    font=("Helvetica", 15, "bold"),
    bg="#FCE4EC",
    fg="#7B1FA2",
)
score_label.pack(pady=15)

again_btn = tk.Button(
    root,
    text="🔄 Play Again",
    font=("Helvetica", 13, "bold"),
    width=16,
    bg="#CE93D8",
    fg="white",
    activebackground="#BA68C8",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=play_again,
)
again_btn.pack(pady=8)

reset_btn = tk.Button(
    root,
    text="🗑 Reset Score",
    font=("Helvetica", 13, "bold"),
    width=16,
    bg="#AB47BC",
    fg="white",
    activebackground="#8E24AA",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=reset_score,
)
reset_btn.pack()

root.mainloop()