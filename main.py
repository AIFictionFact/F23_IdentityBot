# Import openai and os
import os
import openai

# Import interviewer and conversation modules
import interviewer
import conversation

def main():

    # Load key
    keyfile = open("API_KEY.txt", "r")
    openai.api_key = keyfile.readline()
    keyfile.close()

    # Intro to the program
    print("Welcome to IdentityBot, a program that will simulate any person of your choice.")

    # Interview
    print()
    print("To begin, we will conduct an interview.")
    print("Please answer each question as accurately as you can.")
    print()

    # Choose either manual input or import file
    user_input = ""
    while (user_input != "1" and user_input != "2"):
        user_input = input("Would you like to manually respond or load a file? Enter 1 to manually respond, 2 to input a file. ").strip()

    user_responses = {}
    subject_responses = {}
    name = ""

    # Manual input answers
    if user_input == "1":
        print()
        print("In this interview, you can skip questions at any time. Just press enter to move on.")
        print()
        print("Part 1: Responses from you")
        print("In this stage of the interview, we will simulate your subject asking you questions. Please respond from your perspective.")
        print()
        
        user_responses, name = interviewer.interview("user_questions.txt")
        #print(user_responses)      

        print()
        print("Part 2: Responses from your subject")
        print("In the second stage of the interview, we will ask about the subject to gain a better understanding of who they are as a person.")
        print("In this section, answer the questions as if you were your subject. Respond as you think they would to these questions.")
        print()

        subject_responses, _ = interviewer.interview("subject_questions.txt")

    # Import file
    else:
        filename = input("Please enter the file for user responses: ").strip()
        user_responses, name = interviewer.load_dictionary(filename)
        filename = input("Please enter a file for subject responses: ")
        subject_responses, _ = interviewer.load_dictionary(filename)
    #print(user_responses)
    #print(subject_responses)

    print()

    user_input = ""
    while (user_input.lower() != "yes" and user_input.lower() != "no"):
        user_input = input(f"[Optional] Would you like to import texts between you and {name}? Please respond yes or no. ").strip()

    if user_input.lower() == "yes":
        # Import texts
        pass

    # Train the AI
    #model = conversation.train_model(user_responses, subject_responses)
    model = "gpt-3.5-turbo"

    # Have a conversation
    conversation.conduct_conversation(model, user_responses, subject_responses, name)
    

if __name__ == "__main__":
    main()