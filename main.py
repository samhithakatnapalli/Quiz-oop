from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    questions = Question(question_text, question_answer)
    question_bank.append(questions)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nYour final score is: {quiz.score}/{quiz.question_number}")
if quiz.score == quiz.question_number:
    print("Perfect Score!")
elif quiz.score >= 5:
    print("Nice Score!")
else:
    print("Aww, your final score is a bit low. You can try again if you want!")



