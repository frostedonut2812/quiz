
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(answer,current_question.answer)

    def still_has_questions(self):
        if self.question_number <= len(self.question_list):
            return True 
        else:
            return False

    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("you got it right congratulations")
        else:
            print("sorry that was wrong")
        print(f"the correct answer was {correct}")
