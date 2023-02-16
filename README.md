# Overview

This chatbot is designed to help users track their emotions and triggers, and provide a record for them to refer to during therapy. The chatbot is built using Python and the Python-Telegram-Bot library, and it stores diary card data in an Excel spreadsheet for each unique user.

# Requirements

To use this chatbot, you will need the following:

A Telegram account
A Telegram bot token
Python 3.6 or higher
The Python-Telegram-Bot library
The openpyxl library
Installation

Clone this repository or download the code as a zip file.
Install Python 3.6 or higher on your system, if it is not already installed.
Install the required Python libraries by running the following command in the terminal:
```
pip install python-telegram-bot openpyxl
```
Replace YOUR_TELEGRAM_BOT_TOKEN in the code with your Telegram bot token.
Run the Python script by running the following command in the terminal:
```
python diary_card_bot.py
```
Start a conversation with your bot in Telegram by searching for the bot username and sending a message to it.
# Usage

To use the chatbot, follow these steps:

Start a conversation with your bot by sending it a message.
The bot will ask you to enter your emotion for the day. Enter your emotion as a text message.
The bot will ask you what triggered your emotion. Enter the trigger as a text message.
The bot will ask if you have any notes to add. Enter any notes you want to add as a text message.
The bot will confirm that your diary card has been saved to the Excel file.
To cancel the diary card at any time, type /cancel in the chat.

# Customization

You can customize the chatbot to meet your specific requirements by modifying the code. Here are some examples of customizations you could make:

Add more conversation states and message handlers to ask the user for additional information, such as the intensity of their emotion or trigger.
Change the message prompts and responses to match the language and tone of your therapy program.
Modify the Excel file storage to use a different database or storage solution.
Add error handling and security measures to protect user data.

# Conclusion

This chatbot provides a simple and convenient way for users to track their emotions and triggers, and can serve as a valuable tool for dialectical behavior therapy. By customizing the code and adding additional features, you can create a chatbot that meets your specific therapy program requirements.
