from html import unescape

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = unescape(self.current_question.text)

        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: str) -> int:
        if user_answer == self.current_question.answer:
            return 1
        else:
            return 0

