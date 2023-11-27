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
    name = ""
    for line in file:
        line = line.split("|")
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        # Skip blank responses
        if line[1] == "":
            continue
        if line[0] == "How do you refer to this person?":
            name = line[1]
        dictionary[line[0]] = line[1]
    return dictionary, name

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
        print("Part 1: Responses from you")
        print("In this stage of the interview, we will ask about you and your subject, from your perspective.")
        
        user_responses, name = interviewer.interview("user_questions.txt")
        #print(user_responses)      

        print()
        print("Part 2: Responses from your subject")
        print("In the second stage of the interview, we will ask about the subject to gain a better understanding of who they are as a person.")
        print("In this section, answer the questions AS IF YOU WERE YOUR SUBJECT. Pretend you are your subject, and respond as you think they would to these questions.")

        subject_responses, _ = interviewer.interview("subject_questions.txt")

    # Import file
    else:
        filename = input("Please enter the file for user responses: ").strip()
        user_responses, name = load_dictionary(filename)
        filename = input("Please enter a file for subject responses: ")
        subject_responses, _ = load_dictionary(filename)
    #print(user_responses)
    #print(subject_responses)

    print()

    # Train the AI
    #model = conversation.train_model(user_responses, subject_responses)
    model = "gpt-3.5-turbo"

    # Have a conversation
    conversation.conduct_conversation(model, user_responses, subject_responses, name)
    

if __name__ == "__main__":
    main()