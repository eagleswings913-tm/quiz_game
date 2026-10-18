
# ask the questions
# check if the answer is correct
# check if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.correct_answer = self.current_question.answer
        self.question_number += 1
        return f'Q.{self.question_number}: {self.current_question.text} (True/False)?: '
        # user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        # self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
