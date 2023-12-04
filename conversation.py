'''
This file conducts a conversation with the user and the OpenAI API,
which takes on the personality of the subject by fine tuning the API.
'''
import openai

#client = OpenAI(api_key=api_key)

from textblob import TextBlob

#self.client = OpenAI(api_key=api_key)


class IdentityBot:
    def __init__(self, api_key, name, user_responses, subject_responses, model="gpt-3.5-turbo"):
        self.name = name
        self.user_responses = user_responses
        self.subject_responses = subject_responses
        self.model = model
        openai.api_key = api_key  # Set the API key using openai.api_key

        self.conversation_history = []
        self.tuning_data = []

        self.tune_model()

    def analyze_sentiment(self, text):
        '''
        Analyzes the sentiment of text using TextBlob
        Returns positive, neutral, or negative
        '''
        analysis = TextBlob(text)
        return "positive" if analysis.sentiment.polarity > 0 else "neutral" if analysis.sentiment.polarity == 0 else "negative"

    def tune_model(self):
        '''
        Fine-tunes the API given a dictionary of user responses, subject responses, and the subject's name
        This establishes the system role telling the API to respond as if they were the subject
        It also gives examples of user/assistant roles through fine tuning
        Returns the tuning data as a list of dictionaries
        '''

        # System role is just the person's name
        self.tuning_data.append({"role": "system", "content": f"Can you respond to the following questions as if you were {self.name}?"})

        # First sample prompt, to solidify the API is the subject's name
        self.tuning_data.append({"role": "user", "content": "Who are you?"})
        self.tuning_data.append({"role": "assistant", "content": f"I'm {self.name}, of course."})

        # User questionnaire is the assistant asking questions and the user responding
        for question in self.user_responses.items():
            self.tuning_data.append({"role": "assistant", "content": question[0]})
            self.tuning_data.append({"role": "user", "content": question[1]})

        # Subject questionnaire is the user asking questions and the assistant responding
        for question in self.subject_responses.items():
            self.tuning_data.append({"role": "user", "content": question[0]})
            self.tuning_data.append({"role": "assistant", "content": question[1]})

        return self.tuning_data

    def get_gpt_response(self, conversation_history):
        '''
        Returns the response of the API based on the conversation history
        '''
        try:
            response = openai.ChatCompletion.create(model=self.model,
            messages=conversation_history)
            return response.choices[0].message['content']
        except Exception as e:
            print("An error occurred with the OpenAI API:", e)
            return "Error: Could not generate a response."

    def chat_with_bot(self, user_message, trained_context):
        '''
        Sends a user message to the bot, and returns the bot's response
        '''
        sentiment = self.analyze_sentiment(user_message)
        full_conversation_history = trained_context + self.conversation_history.copy()
        full_conversation_history.append({"role": "user", "content": f"{user_message}, this message is in a {sentiment} tone."})
        
        bot_message = self.get_gpt_response(full_conversation_history)
        
        self.conversation_history.append({"role": "assistant", "content": bot_message})
        
        return bot_message

    def conduct_conversation(self, user_message):
        '''
        Runs a loop to conduct the entire conversation with the bot
        '''
        #trained_context = self.tune_model(self.user_responses, self.subject_responses)
        #stop_word = "stop"

        bot_response = self.chat_with_bot(user_message, self.tuning_data)

        return bot_response
