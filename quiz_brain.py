class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        ask_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ{self.question_number}. {ask_question.text}.\nEnter your answer: ").lower()
        self.check_answer(answer, ask_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer.lower():
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer}\nYour current score is: {self.score}/{self.question_number}")

        else:
            print("Wrong answer")
            print(f"You got it right!\nThe correct answer was: {correct_answer}\nYour current score is: {self.score}/{self.question_number}")


