import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz_brain = quiz_brain
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # self.window.minsize(500, 550)

        self.canvas = tk.Canvas(self.window, height=250, width=300)
        self.question = self.canvas.create_text(150, 125, text="Question Text",
                                                fill=THEME_COLOR, font=("Arial", 20, "italic"),
                                                width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = tk.Button()
        true_image = tk.PhotoImage(file=f"images/true.png")
        self.true_button.config(image=true_image, highlightthickness=0,
                                padx=30, pady=50, bd=0, command=self.true_check)
        self.true_button.grid(column=0, row=2)

        self.false_button = tk.Button()
        false_image = tk.PhotoImage(file=f"images/false.png")
        self.false_button.config(image=false_image, highlightthickness=0,
                                 padx=30, pady=50, bd=0, command=self.false_check)
        self.false_button.grid(column=1, row=2)

        self.score_label = tk.Label(text=f"score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, sticky="s")
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def feedback(self, check):

        def cooldown(time):

            if time > 0:
                self.window.after(1000, cooldown, time - 1)
            else:
                self.canvas.config(bg="white")
                self.canvas.itemconfig(self.question, fill=THEME_COLOR)
                if self.quiz_brain.still_has_questions():
                    self.get_next_question()
                else:
                    self.canvas.itemconfig(self.question,
                                           text=f"That's all the questions!\nYou scored {self.score}/10")
                    self.window.after(1000, self.window.quit)

        self.score += check
        self.score_label.config(text=f"score: {self.score}")

        if check == 1:
            self.canvas.config(bg="green")
        elif check == 0:
            self.canvas.config(bg="red")

        self.canvas.itemconfig(self.question, fill="white")
        cooldown(1)

    def true_check(self):
        self.feedback(self.quiz_brain.check_answer("True"))

    def false_check(self):
        self.feedback(self.quiz_brain.check_answer("False"))


