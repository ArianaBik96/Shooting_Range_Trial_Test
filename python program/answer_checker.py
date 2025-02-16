import math

class Answer_Checker:
    def __init__(self, user_answers: dict, total_questions: int):
        self.score = 0  # Initialize score
        self.user_answers = user_answers  # Store user_answers correctly
        self.amount_of_questions = total_questions  # Store the total number of questions
        self.check_score(self.user_answers)  # Call check_score without arguments

    def check_score(self, user_answers):
        
        print("Made by Ariana")
        print("📊 Quiz Results")
        
        for question in user_answers:
            if user_answers[question][0] == user_answers[question][2]:
                self.score += 1

        print("\033[1m🏆 Final Score:\033[0m" + str(self.score) + "/" + str(self.amount_of_questions) + "\n")
        if self.score >= math.ceil((60/100)* self.amount_of_questions):
            print("\033[1m🎉 Congratulations! You passed the quiz!\033[0m")
            print("You passed the quiz with a score of " + str(round((self.score/self.amount_of_questions)*100,2)) + "% \n")
        else:
            print("\033[1m💔 Sorry, You failed the quiz!\033[0m")
            print("You failed the quiz with a score of " + str(round((self.score/self.amount_of_questions)*100,2)) + "% \n\n")             

        self.check_results(user_answers)

    def check_results(self, user_answers): 
        
        questionCounter = 0
        total_time_taken = 0
        for question in user_answers:
            questionCounter += 1
            if user_answers[question][0] == user_answers[question][2]:
                print("\033[1m✅ CORRECT!\033[0m")
                print("Question " + str(questionCounter) + ": " + question)
                print("Your answer: " + user_answers[question][1] + " ✔")
                print("⏳ Time taken: " + str(user_answers[question][4]) + " sec \n")

            else:
                print("\033[1m❌ WRONG!\033[0m")
                print("Question " + str(questionCounter) + ": " + question)
                print("Your answer: " + user_answers[question][1])
                print("Correct answer: " + user_answers[question][3] + " ✔")
                print("⏳ Time taken: " + str(user_answers[question][4]) + " sec \n")
            
            total_time_taken += user_answers[question][4]
            
        print("\n")
        print("Total time taken: " + str(round(total_time_taken,2)) + " sec")
        
