import ollama
import os
import json
import sys
from dotenv import load_dotenv
import datetime

load_dotenv()

MODEL_NAME = os.getenv('MODEL_NAME')
HISTORY_FILE = os.path.join("./chat_history", MODEL_NAME + '_chat_history.json')

def get_response(messages):
    return ollama.chat(model=MODEL_NAME, messages=messages, stream=True)
def print_response(stream, temphistory_content):
    for chunk in stream:
        temphistory_content += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    return temphistory_content

def load_history():
    return json.load(open(HISTORY_FILE, 'r')) if os.path.exists(HISTORY_FILE) else []
def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)
        
def main():
    today = datetime.date.today()
    history = load_history()
    history.append({'role': 'system', 'content': f'Conversation started on {today}'})
    temphistory_content = ""
    while True:
        user_input = input("\nYou: ")
        history.append({'role': 'user', 'content': user_input})
        stream = get_response(history)
        temphistory_content = print_response(stream, temphistory_content)
        try:
            response_content = next(stream)['message']['content']
        except StopIteration:
            history.append({'role': 'assistant', 'content': temphistory_content})
            save_history(history)
            temphistory_content = ""
            print("\n...")

if __name__ == '__main__':
    main()
