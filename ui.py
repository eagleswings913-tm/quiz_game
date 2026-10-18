
import tkinter as tk
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
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
        self.quiz_text = self.canvas.create_text(300, 200, width= 550, text="Quiz Text", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(0,30))

        self.score_label = tk.Label(self.window, text="Score: 0",fg='white',bg=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.score_label.grid(row=0, column=1, padx=0, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=(0,20))
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=(0,20))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_test = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_test)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
