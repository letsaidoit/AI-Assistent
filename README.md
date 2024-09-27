**Ollama Chat History Logger**
======================

**What it does**
-----------

Stores your chat history in a JSON file for later use.
**How it works**
---------------

1. Captures and stores chat conversations in a JSON file.
2. Each conversation is a separate JSON object with messages, timestamps, and user info.
3. Easily load and parse the JSON file to retrieve chat history.

**Features**
-----------

* Stores chat history in a JSON file
* Simple and lightweight
* Uses ollama for advanced logging and dotenv for secure config storage
**Usage**
---------

1. Run the project and start chatting!
2. Chat history is stored in `chat_history/*_chat_history.json`.
3. Load and parse the file to retrieve chat history.

**Required**
-------------

* ollama 
* dotenv


**Commands to create model**
-------------

ollama create <model_name> -f <model file name with location>


