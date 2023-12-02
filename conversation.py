'''
This file conducts a conversation with the user and the OpenAI API,
which takes on the personality of the subject by fine tuning the API.
'''

import openai
from textblob import TextBlob

# Load key
with open("API_KEY.txt", "r") as keyfile:
    openai.api_key = keyfile.readline()

# Dictionary to store conversation history
conversation_history = []

def store_user_data(user_message):
    '''
    Stores a user message in conversation history
    '''
    conversation_history.append({"role": "user", "content": user_message})

def analyze_sentiment(text):
    '''
    Analyzes the sentiment of text using TextBlob
    Returns positive, neutral, or negative
    '''
    analysis = TextBlob(text)
    return "positive" if analysis.sentiment.polarity > 0 else "neutral" if analysis.sentiment.polarity == 0 else "negative"

def tune_model(user_responses, subject_responses, name):
    '''
    Fine-tunes the API given a dictionary of user responses, subject responses, and the subject's name
    This establishes the system role telling the API to respond as if they were the subject
    It also gives examples of user/assistant roles through fine tuning
    Returns the tuning data as a list of dictionaries
    '''
    tuning_data = []

    # System role is just the person's name
    tuning_data.append({"role": "system", "content": f"Can you respond to the following questions as if you were {name}?"})

    # First sample prompt, to solidify the API is the subject's name
    tuning_data.append({"role": "user", "content": "Who are you?"})
    tuning_data.append({"role": "assistant", "content": f"I'm {name}, of course."})

    # User questionnaire is the assistant asking questions and the user responding
    for question in user_responses.items():
        tuning_data.append({"role": "assistant", "content": question[0]})
        tuning_data.append({"role": "user", "content": question[1]})

    # Subject questionnaire is the user asking questions and the assistant responding
    for question in subject_responses.items():
        tuning_data.append({"role": "user", "content": question[0]})
        tuning_data.append({"role": "assistant", "content": question[1]})

    return tuning_data

def get_gpt_response(conversation_history, model):
    '''
    Returns the response of the API based on the conversation history
    '''
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation_history
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        print("An error occurred with the OpenAI API:", e)
        return "Error: Could not generate a response."

def chat_with_bot(user_message, trained_context, model):
    '''
    Sends a user message to the bot, and returns the bot's response
    '''
    sentiment = analyze_sentiment(user_message)
    full_conversation_history = trained_context + conversation_history.copy()
    full_conversation_history.append({"role": "user", "content": f"{user_message}, this message is in a {sentiment} tone."})
    
    bot_message = get_gpt_response(full_conversation_history, model)
    
    conversation_history.append({"role": "assistant", "content": bot_message})
    return bot_message

def conduct_conversation(model, user_responses, subject_responses, name):
    '''
    Runs a loop to conduct the entire conversation with the bot
    '''
    trained_context = tune_model(user_responses, subject_responses, name)
    stop_word = "stop"
    user_message = ""

    print("Welcome to IdentityBot. Type 'stop' at any time to end the chat.")
    print()

    while user_message != stop_word:
        user_message = input("You: ")
        if user_message == stop_word:
            break
        store_user_data(user_message)
        bot_response = chat_with_bot(user_message, trained_context, model)
        print(f"{name}: {bot_response}")
