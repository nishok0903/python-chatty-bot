from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot(
    'SupportBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.db'  # Saves training data to a database
)

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the pre-trained English corpus
trainer.train("chatterbot.corpus.english")

# Example of chatbot interaction
sample_inputs = [
    "Hello",
    "What is your name?",
    "How can I reset my password?",
    "Tell me a joke."
]

for input_text in sample_inputs:
    response = chatbot.get_response(input_text)
    print(f"User: {input_text}\nBot: {response}\n")
