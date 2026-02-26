from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUi

question_bank = []
for question in question_data:
    question_text = question_data['results'][3]['question']
    question_answer = question_data['results'][4]['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)


