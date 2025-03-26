🤖 WHATSAPP BOT ASSISTANT
My second project is for WhatsApp bot ai assistant which replies using open ai model by using some chat history based in that it replies..
This is an automated WhatsApp bot that uses PyAutoGUI for screen automation and OpenAI's GPT API to generate responses. The bot monitors your chat and replies to specific messages using AI.

🚀 FEATURES

Auto-detects messages from a specific sender.

Uses GPT-4o-mini for intelligent responses.

Simulates human-like replies.

Supports both Hindi and English.

🧑‍💻 REQUIREMENTS

Python 3.8 or higher

Chrome installed

WhatsApp Web open in your browser

Microphone and speakers (if needed for notifications)

📦 INSTALL DEPENDENCIES

pip install pyautogui pyperclip openai

🛠 Configuration

API Key: Add your OpenAI API key in the code.

client = OpenAI(api_key="your-openai-api-key")

Sender's Name: Update the name of the sender whose messages you want to respond to.

sender_name="Ravi Chachu"

Coordinates Adjustment: You may need to adjust the coordinates for your screen using pyautogui.position().

🕹 HOW TO RUN

Open WhatsApp Web on your browser.

Run the Python script:

python whatsapp_bot.py

The bot will monitor messages and respond when necessary.

📝 USAGE NOTES

Ensure WhatsApp Web remains open and visible on your screen.

The bot uses Ctrl + C to copy messages and responds using AI.

You can stop the bot using Ctrl + C in the terminal.
