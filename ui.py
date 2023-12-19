import tkinter
import quiz_brain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz: quiz_brain.QuizBrain):

        self.quiz = quiz

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tkinter.Label(self.window, text="Score: 0")
        self.score.config(bg=THEME_COLOR, fg="white", font=("Arial", 11, "bold"))
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.canvas.configure(bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_canvas = self.canvas.create_text(
            150,
            125,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )

        accept = tkinter.PhotoImage(file="./images/true.png")
        decline = tkinter.PhotoImage(file="./images/false.png")

        self.true = tkinter.Button(image=accept, highlightthickness=0, command=self.say_yes)
        self.true.grid(column=0, row=2)

        self.false = tkinter.Button(image=decline, highlightthickness=0, command=self.say_no)
        self.false.grid(column=1, row=2)

        self.change_question()

        self.window.mainloop()

    def change_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_canvas, text=self.quiz.next_question())
            self.true.config(state="active")
            self.false.config(state="active")
        else:
            self.canvas.itemconfig(self.question_canvas, text="You've completed the quiz!")

    def show_result(self, answer: bool):
        if answer:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        if self.quiz.still_has_questions():
            self.quiz.current_question = self.quiz.question_list[self.quiz.question_number]
        self.true.config(state="disabled")
        self.false.config(state="disabled")
        self.window.after(1000, self.change_question)

    def say_yes(self):
        self.show_result(self.quiz.check_answer("True"))

    def say_no(self):
        self.show_result(self.quiz.check_answer("False"))
