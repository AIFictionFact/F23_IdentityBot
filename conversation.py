import openai
from textblob import TextBlob

# Load key
with open("API_KEY.txt", "r") as keyfile:
    openai.api_key = keyfile.readline()

# Dictionary to store conversation history
conversation_history = []

def store_user_data(user_message):
    conversation_history.append({"role": "user", "content": user_message})

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "positive" if analysis.sentiment.polarity > 0 else "neutral" if analysis.sentiment.polarity == 0 else "negative"

def train_model(user_responses, subject_responses):
    training_data = []
    content = "Can you respond to the next questions as if you were this person?"
    # System role is based on the user questionaire
    for question in user_responses.items():
        content += " " + question[0]
        content += " " + question[1]
    training_data.append({"role": "system", "content": content})   

    # User and Assitant roles are based on subject questionaire
    for question in subject_responses.items():
        training_data.append({"role": "user", "content": question[0]})
        training_data.append({"role": "assistant", "content": question[1]})

    print(training_data)
    return training_data

def get_gpt_response(conversation_history, model):
    # Debugging: Print the conversation history and model to check structure
    print("Sending to OpenAI API:", conversation_history, model)

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
    sentiment = analyze_sentiment(user_message)
    full_conversation_history = trained_context + conversation_history.copy()
    full_conversation_history.append({"role": "user", "content": f"{user_message} [Sentiment: {sentiment}]"})
    
    bot_message = get_gpt_response(full_conversation_history, model)
    
    conversation_history.append({"role": "assistant", "content": bot_message})
    return bot_message

def conduct_conversation(model, user_responses, subject_responses):
    trained_context = train_model(user_responses, subject_responses)
    stop_word = "stop"
    response = ""

    print("Welcome to IdentityBot. Type 'stop' at any time to end the chat.")
    print("Hi there! It's been a while. How have you been doing?")

    while response != stop_word:
        user_message = input("You: ")
        store_user_data(user_message)
        bot_response = chat_with_bot(user_message, trained_context, model)
        print(f"Bot: {bot_response}")
