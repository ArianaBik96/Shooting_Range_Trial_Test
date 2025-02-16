import streamlit as st
import random
import time
import import_questions_json
import Streamlit.answer_checker_str as answer_checker_str

class QuestionManager:
    def __init__(self, amount_of_questions: int, data: list):
        self.amount_questions = amount_of_questions
        self.questions_dict = data
        self.user_answers = {}  # Stores user answers, correct answers, and time taken
        self.questions_asked = []  # List to track asked questions
        self.ask_questions()  # Call method to start the quiz

        answer_checker_str.Answer_Checker(self.user_answers, self.amount_questions)
    
    def clear_terminal(self):
        """Clears the terminal screen."""
        st.empty()  # Streamlit does not have a direct equivalent, but this clears output dynamically
    
    def select_random_question(self):
        """Select a random question that hasn't been asked yet."""
        available_questions = [q for q in self.questions_dict if q["question"] not in self.questions_asked]
        if available_questions:
            selected_question = random.choice(available_questions)
            self.questions_asked.append(selected_question["question"])
            return selected_question
        else:
            return None  # No more questions available
    
    def ask_questions(self):
        self.clear_terminal()
        """Ask questions and store responses."""
        st.write("### Please click on the correct answer.")
        if len(self.questions_asked) == len(self.questions_dict):
            st.write("All questions have been asked.")
        else:
            for _ in range(self.amount_questions):
                selected_question = self.select_random_question()
                if not selected_question:
                    break
                
                question = selected_question["question"]
                answers = selected_question["answers"]
                correct_answer = selected_question["correct"]
                
                st.write(f"**{question}**")
                
                col1, col2, col3 = st.columns(3)
                answer_clicked = None
                
                if col1.button(f"A. {answers[0]}"):
                    answer_clicked = "A"
                if col2.button(f"B. {answers[1]}"):
                    answer_clicked = "B"
                if col3.button(f"C. {answers[2]}"):
                    answer_clicked = "C"
                
                if answer_clicked:
                    start_time = time.time()
                    user_choice = answer_clicked
                    end_time = time.time()
                    elapsed_time = round(end_time - start_time, 2)
                    
                    answer_index = ord(user_choice) - ord('A')
                    answer_full = answers[answer_index]
                    
                    correct_index = ord(correct_answer) - ord('A')
                    correct_full = answers[correct_index]
                    
                    self.store_answer(question, user_choice, answer_full, correct_answer, correct_full, elapsed_time)
                    
                    st.success("Answer submitted!")
                    time.sleep(1.5)
                    st.experimental_rerun()
                  
                self.clear_terminal()
    
    def store_answer(self, question, answer, answer_full, correct, correct_full, time_taken):
        """Store all relevant answer details."""
        self.user_answers[question] = [answer, answer_full, correct, correct_full, time_taken]

# Initialize Streamlit app
st.title("Quiz Application")

# Example usage
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

if not st.session_state.quiz_started:
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        # Load questions (replace with actual data loading)
        questions_data = import_questions_json.load_questions()
        QuestionManager(5, questions_data)  # Example with 5 questions