
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_bank.append(Question(q_text=question["text"], q_answer=question["answer"]))
# print(question_bank[0].question + ' and ' + question_bank[0].answer)

quiz_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface()

# while quiz_brain.still_has_questions():
#     quiz_brain.next_question()

print('Quiz is completed')
print(f'Your final score was: {quiz_brain.score}/{quiz_brain.question_number}')
