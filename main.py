from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    package = Question(question["text"], question["answer"])
    question_bank.append(package)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
