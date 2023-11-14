'''
This file conducts an interview with the user and saves their responses, returning
them at the end.

It doesn't need access to the OpenAI API because it's simply asking questions and tracking
the responses.
'''

def interview_about_self():
    # Dictionary to store responses
    responses = {}
    responses["name"] = input("What is your name? ")

    return responses

def interview_about_subject():
    # Dictionary to store responses
    responses = {}
    responses["name"] = input("What is the subject's name? ")

    return responses
    