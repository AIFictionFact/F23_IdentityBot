# Setup

import os
import openai

# Load your API key from an environment variable or secret management service
keyfile = open("API_KEY.txt", "r")
openai.api_key = keyfile.readline()
keyfile.close()

# Intro to the program
print("Welcome to IdentityBot, a program that will simulate anyone in your life.")

# Interview user
subject_name = input("What is the name of the person you want to talk to?")


# Establish messages based on interview responses
messages = [{'role': 'system', 'content': 'training content goes here'}]