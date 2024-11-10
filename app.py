import pickle, re
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from datetime import datetime, date
from advanced import Data_Attribute, Date_Timer, Command

app = Flask(__name__)

# Data
my_data = Data_Attribute()._load_()

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Get the message the user sent to your WhatsApp number
    incoming_msg = request.form.get('Body').lower()

    # Create a Twilio MessagingResponse object
    response = MessagingResponse()

    # Greeting Message
    if 'hello' in incoming_msg:
        reply = "Hello! How can I assist you today?"
    elif 'bye' in incoming_msg:
        reply = "Goodbye! Have a nice day!"
    else:
        reply = "I didn't understand that. Could you say that again?"

    # Command Message
    removed_command = Command(incoming_msg)
    if "/add" in incoming_msg:
        Data_Attribute()._add_(removed_command)
        reply = Data_Attribute()._display_(my_data)
    elif "/remove" in incoming_msg:
        pass
    elif "/show" or "/homework" in incoming_msg:
        reply = Data_Attribute()._display_(my_data)
    
    # Add the reply to the response object
    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
