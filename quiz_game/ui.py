from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image, ImageTk

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        
        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Welcome to Quizler!",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR,   
            )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)
        
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=2, pady=20, columnspan=2)
        
        true_image = Image.open("quiz_game/image/true.png")
        true_image = true_image.resize((50, 50), Image.Resampling.LANCZOS)  # Resize to 50x50 or any size you want
        self.true_image = ImageTk.PhotoImage(true_image)
        self.true_button = Button(self.window, image=self.true_image, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
        
        false_image = Image.open("quiz_game/image/false.png")
        false_image = false_image.resize((50, 50), Image.Resampling.LANCZOS)  # Resize to 50x50 or any size you want
        self.false_image = ImageTk.PhotoImage(false_image)
        self.false_button = Button(self.window, image=self.false_image, command=self.false_pressed)
        self.false_button.grid(row=2, column=2, columnspan=2, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
  
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

        
