import json
from tkinter import Tk, Label, Button, Radiobutton, StringVar, messagebox

# Load questions from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Quiz Application Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.questions = load_questions()
        self.current_question = 0
        self.score = 0
        self.selected_answer = StringVar()
        self.total_questions = len(self.questions)

        self.setup_ui()

    def setup_ui(self):
        # Question Label
        self.question_label = Label(self.root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        # Options (Radiobuttons)
        self.options = []
        for i in range(4):
            rb = Radiobutton(self.root, text="", font=("Arial", 14), variable=self.selected_answer, value="", wraplength=400)
            rb.pack(anchor="w", padx=50, pady=5)
            self.options.append(rb)

        # Navigation Buttons
        self.next_button = Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Load First Question
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}/{self.total_questions}: {question_data['question']}")
        self.selected_answer.set("")
        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if self.selected_answer.get() == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        # Check if the answer is correct
        correct_answer = self.questions[self.current_question]["answer"]
        if self.selected_answer.get() == correct_answer:
            self.score += 1

        # Move to the next question or show results
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {self.total_questions}!")
        self.root.destroy()

# Main Function
if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()
