'''
This file conducts an interview with the user and saves their responses, returning
them at the end.

It doesn't need access to the OpenAI API because it's simply asking questions and tracking
the responses.
'''

def interview(filename):
    # Dictionary to store responses
    responses = {}
    # Open text file of questions
    questions = open(filename, "r")
    for q in questions:
        q = q.strip()
        # If it's a question
        if "?" in q:
            response = input(q + " ").strip()
            # If they didn't skip, save the response
            if response != "":
                responses[q] = response
        # Otherwise just print it
        else:
            print(q)
    questions.close()

    return responses


    