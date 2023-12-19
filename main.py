from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

question_bank = []

for questions in question_data:
    text = questions["question"]
    question = questions["correct_answer"]
    created_question = Question(text, question)
    question_bank.append(created_question)

quiz = QuizBrain(question_bank)
qui = ui.UserInterface(quiz)
