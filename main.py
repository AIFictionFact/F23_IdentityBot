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
    print("Part 1: Questions about you")
    print("In this stage of the interview, we will ask about you to better understand your preferences and personality.")
    
    user_responses = interviewer.interview("user_questions.txt")
    print(user_responses)

    print()
    print("Part 2: Questions about your subject")
    print("In the second stage of the interview, we will ask about the subject athat you wish to have a conversation with to gain a better understanding of who they are as a person.")
    
    subject_responses = interviewer.interview("subject_questions.txt")

    print()

    # Train the AI
    model = conversation.train_model(user_responses, subject_responses)

    # Have a conversation
    conversation.conduct_conversation(model, user_responses, subject_responses)
    

if __name__ == "__main__":
    main()