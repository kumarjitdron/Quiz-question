from question_model import Question
from data import question_data
from quiz_brain import quizbrain

question_bank = []
for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)


quiz= quizbrain(question_bank)
while(quiz.still_has_ques()) :
    quiz.ques_ask()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")