from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

my_quiz = QuizBrain(question_bank)

for _ in question_bank:
    my_quiz.next_question()
    my_quiz.check_answer()

print("You have completed the quiz.")
print(f"your final score is {my_quiz.score}/{my_quiz.question_number}.")
