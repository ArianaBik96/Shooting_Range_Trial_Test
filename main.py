"""import os
import sys
import import_questions_json
import question_manager  # This is the module, avoid reusing its name

# Function to get correct path for the JSON file
def get_resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller .exe
    if getattr(sys, 'frozen', False):  # Running as an .exe
        base_path = sys._MEIPASS
    else:  # Running as a script
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Path to JSON file (adjust filename if needed)
json_path = get_resource_path("vragenlijst_formatted_letters.json")

count_of_quizzes_done = 0
user_choice = ""

if user_choice == "1":
    exit()
elif user_choice == "2" or user_choice == "" or count_of_quizzes_done == 0:
    while user_choice == "2" or user_choice == "":
        while True:  # Keep asking until a valid number is entered
            user_input = input("How many questions would you like to answer? ").strip()

            if not user_input.isdigit():  # Check if input is not a number
                print("\n\033[91m\033[1mInvalid input. Please enter a positive number.\033[0m")
                continue  # Restart loop

            user_input = int(user_input)  # Convert input to integer
            
            if user_input <= 0:  # Check if it's a positive number
                print("\n\033[91m\033[1mPlease enter a number greater than zero.\033[0m")
                continue  # Restart loop
                
            break  # Exit loop when valid input is given

        # Pass the correct JSON file path
        quiz_manager = question_manager.QuestionManager(user_input, import_questions_json.import_Questions_Json(json_path))

        user_choice = input("\n\033[91m\033[1mPress 1 to exit the program, or Press 2 to start again.\033[0m\n")
        count_of_quizzes_done += 1
"""
import os
import sys
import import_questions_json
import question_manager  # This is the module, avoid reusing its name

# Function to get correct path for the JSON file
def get_resource_path(relative_path):
    """ Get absolute path to resource, works for both Nuitka and normal execution """
    if getattr(sys, 'frozen', False):  # Running as a compiled executable
        base_path = os.path.dirname(sys.executable)  # Nuitka places files next to the .exe
    else:  # Running as a normal Python script
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Path to JSON file
json_path = get_resource_path("vragenlijst_formatted_letters.json")

count_of_quizzes_done = 0
user_choice = ""

if user_choice == "1":
    exit()
elif user_choice in ["2", ""] or count_of_quizzes_done == 0:
    while user_choice in ["2", ""]:
        while True:  # Keep asking until a valid number is entered
            user_input = input("How many questions would you like to answer? ").strip()

            if not user_input.isdigit():  # Check if input is not a number
                print("\n\033[91m\033[1mInvalid input. Please enter a positive number.\033[0m")
                continue  # Restart loop

            user_input = int(user_input)  # Convert input to integer
            
            if user_input <= 0:  # Check if it's a positive number
                print("\n\033[91m\033[1mPlease enter a number greater than zero.\033[0m")
                continue  # Restart loop
                
            break  # Exit loop when valid input is given

        # Pass the correct JSON file path
        quiz_manager = question_manager.QuestionManager(user_input, import_questions_json.import_Questions_Json(json_path))

        user_choice = input("\n\033[91m\033[1mPress 1 to exit the program, or Press 2 to start again.\033[0m\n")
        count_of_quizzes_done += 1
