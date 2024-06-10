# SCORM Test Decoder Telegram Bot

![Build Status](https://img.shields.io/github/actions/workflow/status/Radio125/SCORM-Test-Decoder-Telegram-Bot/main.yml?branch=main)
![License](https://img.shields.io/github/license/Radio125/SCORM-Test-Decoder-Telegram-Bot)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [How to Use](#how-to-use)
- [Example Result](#example-result)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

<details id="description">
  <summary>### Description</summary>
  The **SCORM Test Decoder Telegram Bot** is designed to facilitate the extraction and decoding of SCORM (Sharable Content Object Reference Model) test questions and answers from JSON files. It supports SCORM versions 1.2 and 2004, making it a versatile tool for analyzing test data.
</details>

<details id="features">
  <summary>### Features</summary>
  - **Upload and Decode SCORM Files**: Users can upload `data-1.json` files containing encrypted SCORM test questions. The bot decrypts the data and provides a readable output.
  - **SCORM Test Parsing**: The bot automatically identifies the type of each question and provides the correct answers.
  - **Real-Time Responses**: Provides immediate feedback by decoding and displaying test content upon file upload.
  - **Comprehensive Overview**: Displays all test questions and answers in a single window for quick review.
</details>

<details id="how-to-use">
  <summary>### How to Use</summary>
  1. **Start the Bot**: Add the bot to your Telegram contacts and start a chat.
  2. **Upload SCORM JSON File**: Send the `data-1.json` file containing SCORM test data to the bot.
  3. **Receive Decoded Content**: The bot processes the file and returns the decoded questions and answers in a readable format.
</details>

<details id="example-result">
  <summary>### Example Result</summary>
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
</details>

<details id="installation">
  <summary>### Installation</summary>
  To set up the bot locally:
  1. **Clone the Repository**:
     <details>
       <summary>Click to copy</summary>
       ```bash
       git clone https://github.com/Radio125/SCORM-Test-Decoder-Telegram-Bot.git
       ```
     </details>
  2. **Navigate to the Directory**:
     <details>
       <summary>Click to copy</summary>
       ```bash
       cd SCORM-Test-Decoder-Telegram-Bot
       ```
     </details>
  3. **Create a Virtual Environment (optional but recommended)**:
     <details>
       <summary>Click to copy</summary>
       ```bash
       python -m venv venv
       ```
     </details>
  4. **Activate the Virtual Environment**:
     <details>
       <summary>Click to copy for Windows</summary>
       ```bash
       venv\Scripts\activate
       ```
     </details>
     <details>
       <summary>Click to copy for macOS/Linux</summary>
       ```bash
       source venv/bin/activate
       ```
     </details>
  5. **Install Dependencies**:
     <details>
       <summary>Click to copy</summary>
       ```bash
       pip install aiogram==3.7.0
       ```
     </details>
  6. **Run the Bot**:
     <details>
       <summary>Click to copy</summary>
       ```bash
       python bot.py
       ```
     </details>
</details>

<details id="configuration">
  <summary>### Configuration</summary>
  **Bot Token**: Replace the placeholder token in the `config.py` file with your actual Telegram Bot API token.
  **SCORM Files**: Ensure SCORM JSON files are properly formatted for the bot to decode and process them effectively.
</details>

<details id="contributing">
  <summary>### Contributing</summary>
  If you would like to contribute to the development of this bot, please feel free to fork the repository and submit pull requests. Any suggestions or bug reports are also welcome via GitHub issues.
</details>

<details id="author">
  <summary>### Author</summary>
  Created by Radio125. Feel free to download, distribute, and modify the code. A simple like is enough!
</details>

<details id="license">
  <summary>### License</summary>
  This project is licensed under the MIT License - see the LICENSE file for details.
</details>
