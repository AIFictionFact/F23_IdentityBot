'''
This file conducts an interview with the user and saves their responses, returning
them at the end.

It doesn't need access to the OpenAI API because it's simply asking questions and tracking
the responses.
'''

def interview_about_user():
    # Dictionary to store responses
    responses = {}
    # Open text file of questions
    questions = open("user_questions.txt", "r")
    for q in questions:
        responses[q] = input(q + " ")
    questions.close()

    return responses

def interview_about_subject():
    # Dictionary to store responses
    responses = {}
    # Open text file of questions
    questions = open("subject_questions.txt", "r")
    for q in questions:
        responses[q] = input(q + " ")
    questions.close()

    return responses
    