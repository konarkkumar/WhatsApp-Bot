import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(api_key = "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",)

last_replied_message = ""

def is_last_message_from_sender(chat_log, sender_name="Ravi Chachu"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ") [-1].strip()
    return sender_name in messages, messages
    
# Step 1: Click on the chrome icon at coordinates (1196, 1047)
pyautogui.click(1181, 1056)
time.sleep(2)  # Wait for the app to open
    
while True:

    # Step 2: Drag to select the text
    pyautogui.moveTo(758, 290)  # Move to the starting position
    pyautogui.dragTo(1799, 972 , duration=1.0, button='left')  # Drag to the end position

    # Step 3: Copy the selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)  # Allow time for copying
    pyautogui.click(670, 272)

    # Step 4: Get copied text from the clipboard
    chat_history = pyperclip.paste()

    is_sender, last_message = is_last_message_from_sender(chat_history)
    if is_sender and last_message != last_replied_message:
        print(f"New message detected: {last_message}")
        # Generate a response using OpenAI
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a person named konark kumar who speaks hindi as well as english. You are from India and you are a coder. You analyse and respond like konark kumar. Output should be the next chat response as (text message only)without date and time."},
            {
                "role": "user",
                "content": chat_history
            }
            ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)

        pyautogui.click(957, 1021)  # Click on input field
        time.sleep(1)  # Wait for focus

        # Step 2: Paste the copied text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for paste action

        # Step 3: Press Enter to send the message
        pyautogui.press('enter')
        
        #Update the last replied message
        last_replied_message = last_message
        
    time.sleep(5)  # Wait for 5 seconds before checking again