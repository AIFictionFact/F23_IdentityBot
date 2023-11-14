'''
This file conducts a conversation between you and the person of your choice
'''
import openai
from textblob import TextBlob  # Import sentimental analyzer

# Load key
with open("API_KEY.txt", "r") as keyfile:
    openai.api_key = keyfile.readline()

# Dictionary to store user data and conversation history
user_data = {}

# Function to store user messages in user_data
def store_user_data(user_id, user_message):
    if user_id not in user_data:
        user_data[user_id] = {"messages": []}
    user_data[user_id]["messages"].append({"role": "user", "content": user_message})

# Function to analyze the sentiment of a text using TextBlob 
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "positive" if analysis.sentiment.polarity > 0 else "neutral" if analysis.sentiment.polarity == 0 else "negative"

# Function to format training data into conversation history
def train_model(user_responses, subject_responses):
    training_data = []
    for question, answer in zip(user_responses.items(), subject_responses.items()):
        training_data.append({"role": "user", "content": question[1]})
        training_data.append({"role": "assistant", "content": answer[1]})
    return training_data

# Function to get response from GPT model
def get_gpt_response(conversation_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    return response.choices[0].message['content']

# Function to chat with the bot
def chat_with_bot(user_id, user_message, trained_context):
    sentiment = analyze_sentiment(user_message)
    conversation_history = trained_context + user_data[user_id]["messages"].copy()
    conversation_history.append({"role": "user", "content": f"{user_message} [Sentiment: {sentiment}]"})
    
    # Get bot's response using GPT model
    bot_message = get_gpt_response(conversation_history)
    
    # Store bot's message in the conversation history
    user_data[user_id]["messages"].append({"role": "assistant", "content": bot_message})
    return bot_message

# Conversation
def conduct_conversation(user_id, user_responses, subject_responses):
    trained_context = train_model(user_responses, subject_responses)
    stop_word = "stop"
    response = ""

    print("Welcome to IdentityBot. Type 'stop' at any time to end the chat.")
    print("Hi there! It's been a while. How have you been doing?")

    while response != stop_word:
        user_message = input("You: ")
        store_user_data(user_id, user_message)
        bot_response = chat_with_bot(user_id, user_message, trained_context)
        print(f"Bot: {bot_response}")
