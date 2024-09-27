import subprocess
import datetime

def create_new_note(note_content):
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    apple_script = f'''
        tell application "Notes"
            set new_note to "{current_date} - {note_content}"
            make new note at end with properties {{name:new_note, body:new_note}}
        end tell
    '''
    subprocess.run(['osascript', '-e', apple_script])

def get_all_notes():
    apple_script = '''
        tell application "Notes"
            set note_list to ""
            repeat with each_note in notes
                set note_list to note_list & (name of each_note) & ", "
            end repeat
            return note_list
        end tell
    '''
    result = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
    note_list = result.stdout.strip().split(', ')
    return note_list
def send_message(recipient, message_content):
    apple_script = f'''
        tell application "Messages"
            set recipient_name to "{recipient}"
            set message_content to "{message_content}"
            tell application "Messages" to send message_content to buddy id "{recipient}"
        end tell
    '''
    subprocess.run(['osascript', '-e', apple_script])

import pyautogui

def send_whatsapp_message(phone_number, message_content):
    # Open WhatsApp using the default application
    pyautogui.hotkey('command', 'space')  # Open Spotlight search
    pyautogui.typewrite('whatsapp')  # Type "WhatsApp"
    pyautogui.press('enter')  # Press Enter to open WhatsApp

    # Wait for WhatsApp to open
    pyautogui.sleep(2)

    # Enter phone number
    pyautogui.typewrite(phone_number)
    pyautogui.press('tab')  # Move focus to the message field
    pyautogui.typewrite(message_content)
    pyautogui.press('enter')  # Press Enter to send the message

# Example usage:
send_whatsapp_message("Arbaz Khan", "Hello from Python!")

# create_new_note("Hello, World!")

# all_notes = get_all_notes()
# print("All Notes:", all_notes)ty44567