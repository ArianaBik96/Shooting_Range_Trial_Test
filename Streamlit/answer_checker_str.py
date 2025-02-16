import streamlit as st
import math

class AnswerChecker:
    def __init__(self, user_answers: dict, total_questions: int):
        self.score = 0  # Initialize score
        self.user_answers = user_answers  # Store user answers correctly
        self.amount_of_questions = total_questions  # Store the total number of questions
        self.check_score()  # Call check_score without arguments
    
    def check_score(self):
        st.write("Made by Ariana")
        st.header("📊 Quiz Results")
        
        for question in self.user_answers:
            if self.user_answers[question][0] == self.user_answers[question][2]:
                self.score += 1
        
        st.subheader(f"🏆 Final Score: {self.score}/{self.amount_of_questions}")
        score_percentage = round((self.score / self.amount_of_questions) * 100, 2)
        
        if self.score >= math.ceil((60/100) * self.amount_of_questions):
            st.success(f"🎉 Congratulations! You passed the quiz with a score of {score_percentage}%")
        else:
            st.error(f"💔 Sorry, You failed the quiz with a score of {score_percentage}%")
        
        self.check_results()
    
    def check_results(self): 
        question_counter = 0
        total_time_taken = 0
        
        for question in self.user_answers:
            question_counter += 1
            is_correct = self.user_answers[question][0] == self.user_answers[question][2]
            
            with st.expander(f"Question {question_counter}: {question}"):
                if is_correct:
                    st.success("✅ CORRECT!")
                    st.write(f"**Your answer:** {self.user_answers[question][1]} ✔")
                else:
                    st.error("❌ WRONG!")
                    st.write(f"**Your answer:** {self.user_answers[question][1]}")
                    st.write(f"**Correct answer:** {self.user_answers[question][3]} ✔")
                
                st.write(f"⏳ Time taken: {self.user_answers[question][4]} sec")
            
            total_time_taken += self.user_answers[question][4]
        
        st.subheader(f"Total time taken: {round(total_time_taken, 2)} sec")
