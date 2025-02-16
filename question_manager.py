import os
import random
import time
import import_questions_json
import answer_checker

class QuestionManager:
    def __init__(self, amount_of_questions: int, data: list):
        self.amount_questions = amount_of_questions
        self.questions_dict = data
        self.user_answers = {}  # Stores user answers, correct answers, and time taken
        self.questions_asked = []  # List to track asked questions
        self.ask_questions()  # Call method to start the quiz

        answer_checker.Answer_Checker(self.user_answers, self.amount_questions)

    def clear_terminal(self):
        """Clears the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")  # Works for Windows and macOS/Linux

    def select_random_question(self):
        """Select a random question that hasn't been asked yet."""
        while True:
            selected_question = random.choice(self.questions_dict)
            if selected_question["question"] not in self.questions_asked:
                self.questions_asked.append(selected_question["question"])
                return selected_question

    def ask_questions(self):
        self.clear_terminal()  # Clear the screen after each question
        print("\n\033[91m\033[1mPlease answer with A, B, or C. Then press enter\033[0m\n")
        """Ask questions and store responses."""
        if len(self.questions_asked) == len(self.questions_dict):
            print("All questions have been asked.")
        else:
            for _ in range(self.amount_questions):
                selected_question = self.select_random_question()
                question = selected_question["question"]
                answers = selected_question["answers"]  # List of answer choices
                correct_answer = selected_question["correct"]  # Letter of correct answer

                print(question)
                print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\n")

                start_time = time.time()
                user_answer = input("Your answer: ").strip().upper()
                print("\n")
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)

                # Validate input: should be exactly one character (A, B, or C)
                if len(user_answer) != 1 or user_answer not in "ABC":
                    answer_full = f"Invalid Answer --> {user_answer}"
                else:
                    answer_index = ord(user_answer) - ord('A')
                    answer_full = answers[answer_index]

                # Get correct answer full text
                correct_index = ord(correct_answer) - ord('A')
                correct_full = answers[correct_index]

                self.store_answer(question, user_answer, answer_full, correct_answer, correct_full, elapsed_time)
                
                time.sleep(1.5)  # Wait for 1.5 seconds before clearing
                self.clear_terminal()  # Clear the screen after each question

            return self.user_answers

    def store_answer(self, question, answer, answer_full, correct, correct_full, time_taken):
        """Store all relevant answer details."""
        self.user_answers[question] = [answer, answer_full, correct, correct_full, time_taken]
