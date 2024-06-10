## SCORM Test Decoder Telegram Bot

### Description

The **SCORM Test Decoder Telegram Bot** is designed to facilitate the extraction and decoding of SCORM (Sharable Content Object Reference Model) test questions and answers from JSON files. It supports SCORM versions 1.2 and 2004, making it a versatile tool for analyzing test data.

### Features

- **Upload and Decode SCORM Files**: Users can upload `data-1.json` files containing encrypted SCORM test questions. The bot decrypts the data and provides a readable output.
  
- **SCORM Test Parsing**: The bot automatically identifies the type of each question and provides the correct answers.

- **Real-Time Responses**: Provides immediate feedback by decoding and displaying test content upon file upload.

- **Comprehensive Overview**: Displays all test questions and answers in a single window for quick review.

### How to Use

1. **Start the Bot**: Add the bot to your Telegram contacts and start a chat.
2. **Upload SCORM JSON File**: Send the `data-1.json` file containing SCORM test data to the bot.
3. **Receive Decoded Content**: The bot processes the file and returns the decoded questions and answers in a readable format.

### Example Result

**Question**: Now match the pairs as they should be:
- **Type**: Matching
- **Answers**:
  - 🔗 Pair 1 part 1 -> Pair 1 part 2
  - 🔗 Pair 2 part 1 -> Pair 2 part 2
  - 🔗 Pair 3 part 1 -> Pair 3 part 2

**Question**: How many blue hairs does Harry Potter have?
- **Type**: Multiple Choice
- **Answers**:
  - ❌ A hundred million
  - ❌ None
  - ✅ Twenty-five
  - ❌ Fifty-four

**Question**: Enter the answer to your question from me, how much does a kilo of raisins cost in raisins?
- **Type**: Text Input

**Question**: What is the sequence of notes?
- **Type**: Sequencing
- **Answers**:
  1️⃣ Do
  2️⃣ Re
  3️⃣ Mi
  4️⃣ Fa
  5️⃣ So
  6️⃣ La
  7️⃣ Ti

**Question**: There are 2 correct answers, try to guess which options are correct:
- **Type**: Multiple Response
- **Answers**:
  - ✅ Second option
  - ✅ Option one
  - ❌ This is the third option
  - ❌ And here is the fourth option
  
### Installation

To set up the bot locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Radio125/SCORM-Test-Decoder-Telegram-Bot.git
   
2. Navigate to the Directory:
   cd SCORM-Test-Decoder-Telegram-Bot

3. Create a Virtual Environment (optional but recommended):
    python -m venv venv

4. Activate the Virtual Environment:
  On Windows:
    venv\Scripts\activate
  On macOS/Linux:
    source venv/bin/activate
   
5. Install Dependencies:
  pip install -r requirements.txt

6. Run the Bot:
  python bot.py

Configuration
Bot Token: Replace the placeholder token in the config.py file with your actual Telegram Bot API token.
SCORM Files: Ensure SCORM JSON files are properly formatted for the bot to decode and process them effectively.
Contributing
If you would like to contribute to the development of this bot, please feel free to fork the repository and submit pull requests. Any suggestions or bug reports are also welcome via GitHub issues.

Author
Created by Radio125. Feel free to download, distribute, and modify the code. A simple like is enough!

License
This project is licensed under the MIT License - see the LICENSE file for details.
