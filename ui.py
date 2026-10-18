
import tkinter as tk
from tkinter import PhotoImage

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window_width = 700
        self.window_height = 650
        self.window.config(bg=THEME_COLOR)
        # 1. Get the screen dimensions
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        # 2. Find the center point coordinates
        self.center_x = int((self.screen_width / 2) - (self.window_width / 2))
        self.center_y = int((self.screen_height / 2) - (self.window_height / 2))
        # 3. Apply the geometry string
        self.window.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}")
        self.window.config(padx=50, pady=20)

        self.canvas = tk.Canvas(self.window, width=600, height=400, highlightthickness=0, bg='white')
        self.quiz_text = self.canvas.create_text(300, 200, text="Quiz Text", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(0,30))

        self.score_label = tk.Label(self.window, text="Score: 0",fg='white',bg=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.score_label.grid(row=0, column=1, padx=0, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=(0,20))
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1, pady=(0,20))



        self.window.mainloop()