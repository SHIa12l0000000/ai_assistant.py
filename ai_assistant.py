# ai_assistant.py

import datetime
import webbrowser

def ai_reply(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! I’m your AI assistant. How can I help you today?"

    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M')}."

    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}."

    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "open google" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don’t understand that command."

# Run assistant in a loop
print("🔵 Basic AI Assistant (Type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    response = ai_reply(user_input)
    print("AI:", response)
    if "goodbye" in response.lower():
        break
      
