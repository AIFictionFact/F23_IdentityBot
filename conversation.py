'''
This file conducts a conversation between you and the person of your choice
'''
import openai
# Load key
keyfile = open("API_KEY.txt", "r")
openai.api_key = keyfile.readline()
keyfile.close()

# Perform initial training of the model
def train_model(self_responses, subject_responses):
    messages = [{'role': 'system', 'content': 'training content goes here'}]

    model = openai.ChatCompletion(model="gpt-3.5-turbo", messages=messages)

    return model

# Conversation
def conduct_conversation(model, self_responses, subject_responses):
    stop_word = "stop"
    response = ""

    while response != stop_word:
        print("here is what the AI says")
        response = input("")
