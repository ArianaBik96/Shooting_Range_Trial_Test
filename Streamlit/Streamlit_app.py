import streamlit as st
import import_questions_json
import question_manager_str  # This is the module, avoid reusing its name

# Function to get correct path for the JSON file
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller .exe"""
    import sys
    import os
    if getattr(sys, 'frozen', False):  # Running as an .exe
        base_path = sys._MEIPASS
    else:  # Running as a script
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Path to JSON file (adjust filename if needed)
json_path = get_resource_path("vragenlijst_formatted_letters.json")

st.title("📋 Quiz Application")

if "count_of_quizzes_done" not in st.session_state:
    st.session_state.count_of_quizzes_done = 0

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if st.session_state.user_choice == "1":
    st.stop()
elif st.session_state.user_choice == "2" or st.session_state.user_choice == "" or st.session_state.count_of_quizzes_done == 0:
    while True:
        user_input = st.text_input("How many questions would you like to answer?", "").strip()
        
        if not user_input.isdigit():
            st.error("Invalid input. Please enter a positive number.")
            continue
        
        user_input = int(user_input)
        
        if user_input <= 0:
            st.error("Please enter a number greater than zero.")
            continue
        
        break
    
    if st.button("Start Quiz"):
        quiz_manager = question_manager_str.QuestionManager(user_input, import_questions_json.import_Questions_Json(json_path))
        st.session_state.count_of_quizzes_done += 1
        