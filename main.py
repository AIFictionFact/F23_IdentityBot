'''
This file contains the main code for IdentityBot.
It uses two other Python files, interviewer.py and conversation.py.

It facilitates conducting a conversation with a subject of the user's choice,
based on their description of the subject, which is used to fine-tune
the OpenAI ChatGPT API to replicate the subject.
'''

# Import openai and system modules
import openai
import time
import sys

# Import our modules
import interviewer
import ui

def delay_print(s):
    '''
    Function to print a string letter by letter
    '''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def main():

    # Load key
    keyfile = open("API_KEY.txt", "r")
    openai.api_key = keyfile.readline()

    keyfile.close()

    # Intro to the program
    intro = "Welcome to IdentityBot, a program that will simulate any person of your choice.\n"
    print("-"*len(intro))
    delay_print(intro)
    print("-"*len(intro))

    # Disclaimers
    print()
    intro = "Disclaimers\n"
    print("-"*len(intro))
    delay_print(intro)
    print("-"*len(intro))

    print("- IdentityBot is an AI bot and not a substitute for professional psychological help.")
    print("- IdentityBot is not a substitute for the person you wish to talk to, it only seeks to artificially replicate them.")
    print("- IdentityBot does not store any of your personal data. It will be discarded after your session.")
    
    user_input = ""
    while user_input.lower() != "yes" and user_input.lower() != "no":
        print()
        user_input = input("Do you acknowledge these disclaimers and wish to continue? Please respond yes or no. ==> ").strip()
        if user_input == "yes":
            break
        if user_input == "no":
            # Exit program if user doesn't agree to disclaimers
            return


    # Interview
    print()
    intro = "Interview\n"
    print("-"*len(intro))
    delay_print(intro)
    print("-"*len(intro))
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
        intro = "Part 1: Responses from you\n"
        print("-"*len(intro))
        delay_print(intro)
        print("-"*len(intro))

        print("In this stage of the interview, we will simulate your subject asking you questions. Please respond from your perspective.")
        print()
        
        user_responses, name = interviewer.interview("user_questions.txt")

        print()
        intro = "Part 2: Responses from your subject\n"
        print("-"*len(intro))
        delay_print(intro)
        print("-"*len(intro))

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

    # Text history - not implemented
    '''
    print()

    user_input = ""
    while (user_input.lower() != "yes" and user_input.lower() != "no"):
        user_input = input(f"[Optional] Would you like to import texts between you and {name}? Please respond yes or no. ").strip()

    if user_input.lower() == "yes":
        # Import texts
        pass
    '''

    # Train the AI
    model = "gpt-3.5-turbo"

    ui.start_ui(openai.api_key, name, user_responses, subject_responses, model)

    # Have a conversation
    #conversation.conduct_conversation(model, user_responses, subject_responses, name)

if __name__ == "__main__":
    main()