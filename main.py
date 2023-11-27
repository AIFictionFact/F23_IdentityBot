# Import openai and os
import os
import openai

# Import interviewer and conversation modules
import interviewer
import conversation

# Load a file into a dictionary, for testing
def load_dictionary(filename):
    file = open(filename, "r")
    dictionary = {}
    for line in file:
        line = line.split("|")
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        # Skip blank responses
        if line[1] == "":
            continue
        dictionary[line[0]] = line[1]
    return dictionary

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

    # Manual input answers
    if user_input == "1":
        print()
        print("Part 1: Responses from you")
        print("In this stage of the interview, we will ask about you to better understand your preferences and personality.")
        
        user_responses = interviewer.interview("user_questions.txt")
        print(user_responses)      

        print()
        print("Part 2: Responses from your subject")
        print("In the second stage of the interview, we will ask about the subject that you wish to have a conversation with to gain a better understanding of who they are as a person.")
        print("In this section, answer the questions AS IF YOU WERE YOUR SUBJECT. Pretend you are your subject, and respond as you think they would to these questions.")

        subject_responses = interviewer.interview("subject_questions.txt")

    # Import file
    else:
        filename = input("Please enter the file for user responses: ").strip()
        user_responses = load_dictionary(filename)
        filename = input("Please enter a file for subject responses: ")
        subject_responses = load_dictionary(filename)
    #print(user_responses)
    #print(subject_responses)

    print()

    # Train the AI
    #model = conversation.train_model(user_responses, subject_responses)
    model = "gpt-3.5-turbo"

    # Have a conversation
    conversation.conduct_conversation(model, user_responses, subject_responses)
    

if __name__ == "__main__":
    main()