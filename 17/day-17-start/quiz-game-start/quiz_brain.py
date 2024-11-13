class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.answer = ""

    def next_question(self):
        self.answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}"
                            f" (True/False)?: ").lower()
        self.question_number += 1

    def check_answer(self):
        if self.answer == self.question_list[self.question_number-1].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")




