CSCI 4970 – Ai in Fiction & Fact
Design Documentation

Title
Project: IdentityBot
Names: Emma Clements (clemee3), Sam Francis(francs3), Annie Xu (xuj18)
Github Link: https://github.com/AIFictionFact/F23_IdentityBot

Project Overview:
IdentityBot aims to simulate conversations with virtual representations of people based on user descriptions. Leveraging the ChatGPT API, it offers personalized interactions, including emotional support and nostalgic conversations.
Goals:
Develop a chatbot that excels at personalizing conversations based on user-provided descriptions
Deliver meaningful emotional support and engagement, providing users with companionship and therapeutic value
Recognize multiple user profiles and refer back to previous conversations, ensuring continuity

Related AI Projects
Replika.ai: Released in 2017, Replika.ai is a chatbot based on the text messages of the creator's friend after their death.
Character.ai: Introduced in beta form in 2022, Character.ai is a chatbot focused on conversations with fictional, historical, and celebrity characters.
ChatGPT: Released in 2022, ChatGPT is an AI language model that uses natural language processing to provide assistance and information on a wide range of subjects.

Functional Requirements
User Profile Creation: Users can create profiles for the individuals they want to simulate conversations with, including their name, characteristics, and communication style.
Personalization: The details from the user profiles will be given as parameters to the ChatGPT AI to influence how it responds to prompts.
Emotional Support: The chatbot can offer comforting advice and support to provide companionship.
Conversation Tracking: The chatbot can refer back to previous prompts and even previous conversations to ensure continuity.

Non-functional Requirements
Quality User Interface: The user interface will be intuitive and accessible for everyone.
Fast Response Times: The chatbot will respond to user input within a reasonable time frame, with a goal of near-instantaneous replies.
Reliable: The chatbot will be reliable, with robust error handling and recovery mechanisms to minimize interruptions.
Maintainable: The chatbot will be developed with maintainability in mind, with clean code and comprehensive documentation, making it easy for developers to update and enhance the application in the future.

System Architecture
The main components are Python and the OpenAI API. The user will enter answers to basic questions, which are processed in Python and passed to the OpenAI API, used to tune its parameters. Then Python uses the OpenAI API to start a conversation with the user, which consists of getting user input, processing it in Python, passing it to OpenAI API, fetching a response, and printing the response in Python. Python is used to store data associated with a user, such as the unique profiles associated with that user, and their conversation history. This data is used to train OpenAI to respond in a convincing way.

Technologies to be Used
Python: Script and Automation, Data Handling, API Integration, Backend Development
OpenAI API: Language Model, Fine-Tuning, Conversation State Management, Sentiment Analysis
GitHub: Version Control, Code Collaboration

User Profiles
Grieving Family Members: Seeking solace and remembrance through conversational memories.
Historians & Biographers: Looking to capture and document the personality and stories of the deceased.
Therapy Clients: Using the chatbot as a therapeutic tool to process grief and loss.
Former Colleagues and Peers: Professionals who value the insights and mentorship they once received.
Close Friends: Seeking to reminisce and experience the personality of the deceased.

UI/UX Design
The UI will be very simple in order to make it easy for the user to understand the program. The program will start with an Intro with a series of open ended questions in order to capture the personality of the person and once the interview stage has completed then it will transition to the conversation where there is a header with some basic information about the person and then a chatlog of the conversation so far.
Interview Stage:
PB: What is the name of the person? 
You: James
PB: How does this James refer to you?
You: Mike
Conversation Stage:
James: Hey Mike! How’s it going? 
You: I’m doing good, how is your dog?
James: He has as much energy as ever, he plays with his squeaky toy every day!

10. Team Roles
Emma – Lead Developer: Responsible for developing the core components of the chatbot, including conversational and personalization features.
Annie – API Integrations: Responsible for integrating, training, and tuning parameters for the external ChatGPT API.
Sam – Quality Assurance: Responsible for testing functionality, identifying and reporting bugs, and ensuring overall quality.

11. Technical Limitations
Limited data set: We are only gathering details about a person through a questionnaire so more intricate aspects of their verbal behaviour might not be able to be recreated without a large data set like text messages or phone calls
Privacy: Using personal information about someone like text messages and phone calls could violate the privacy of those conversations as the person may not consent to their texts being seen by other people
Lack of real-time updates:  The personality of the chatbot will be static meaning if the personality of this person evolves over time the chatbot will not be able to know how this person has changed
User interface: The user interface will not have any animations for visual representation of the person so it will lack the visual aspect of a conversation
Subjectivity -  The way a person perceives someone's personality can be very subjective so being able to capture the personality of someone the way that 
