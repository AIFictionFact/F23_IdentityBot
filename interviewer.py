'''
This file conducts an interview with the user and saves their responses, returning
them at the end.

It doesn't need access to the OpenAI API because it's simply asking questions and tracking
the responses.
'''

def interview(filename):
    # Dictionary to store responses
    responses = {}
    # Name of subject
    name = ""
    # Open text file of questions
    questions = open(filename, "r")
    for q in questions:
        q = q.strip()
        response = input(q + " ").strip()
        if q == "How do you refer to me?":
            name = response
        # If they didn't skip, save the response
        if response != "":
            responses[q] = response
    questions.close()

    return responses, name

# Load a file into a dictionary, for testing
def load_dictionary(filename):
    file = open(filename, "r")
    dictionary = {}
    name = ""
    for line in file:
        line = line.split("|")
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        # Store name
        if line[0] == "How do you refer to me?":
            name = line[1]
        # Skip blank responses
        if line[1] == "":
            continue
        dictionary[line[0]] = line[1]
    return dictionary, name
