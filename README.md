# SCORM (iSpring Learn) Test Decoder Telegram Bot

![Build Status](https://img.shields.io/github/actions/workflow/status/Radio125/SCORM-Test-Decoder-Telegram-Bot/ci.yml?branch=main)
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

## Description
<details>
  <summary>Click to expand</summary>
  <p>The <strong>SCORM Test Decoder Telegram Bot</strong> is designed to facilitate the extraction and decoding of SCORM (Sharable Content Object Reference Model) test questions and answers from JSON files. It supports SCORM versions 1.2 and 2004, making it a versatile tool for analyzing test data.</p>
</details>

## Features
<details>
  <summary>Click to expand</summary>
  <ul>
    <li><strong>Upload and Decode SCORM Files</strong>: Users can upload <code>data-1.json</code> files containing encrypted SCORM test questions. The bot decrypts the data and provides a readable output.</li>
    <li><strong>SCORM Test Parsing</strong>: The bot automatically identifies the type of each question and provides the correct answers.</li>
    <li><strong>Real-Time Responses</strong>: Provides immediate feedback by decoding and displaying test content upon file upload.</li>
    <li><strong>Comprehensive Overview</strong>: Displays all test questions and answers in a single window for quick review.</li>
  </ul>
</details>

## How to Use
<details>
  <summary>Click to expand</summary>
  <ol>
    <li><strong>Start the Bot</strong>: Add the bot to your Telegram contacts and start a chat.</li>
    <li><strong>Upload SCORM JSON File</strong>: Send the <code>data-1.json</code> file containing SCORM test data to the bot.</li>
    <li><strong>Receive Decoded Content</strong>: The bot processes the file and returns the decoded questions and answers in a readable format.</li>
  </ol>
</details>

## Example Result
<details>
  <summary>Click to expand</summary>
  <p><strong>Question</strong>: Match the pairs as they should be:</p>
  <ul>
    <li><strong>Type</strong>: Matching</li>
    <li><strong>Answers</strong>:
      <ul>
        <li>🔗 Pair 1 part 1 -> Pair 1 part 2</li>
        <li>🔗 Pair 2 part 1 -> Pair 2 part 2</li>
        <li>🔗 Pair 3 part 1 -> Pair 3 part 2</li>
      </ul>
    </li>
  </ul>
  <p><strong>Question</strong>: How many blue hairs does Harry Potter have?</p>
  <ul>
    <li><strong>Type</strong>: Multiple Choice</li>
    <li><strong>Answers</strong>:
      <ul>
        <li>❌ A hundred million</li>
        <li>❌ None</li>
        <li>✅ Twenty-five</li>
        <li>❌ Fifty-four</li>
      </ul>
    </li>
  </ul>
  <p><strong>Question</strong>: Enter the answer to your question from me, how much does a kilo of raisins cost in raisins?</p>
  <ul>
    <li><strong>Type</strong>: Text Input</li>
  </ul>
  <p><strong>Question</strong>: What is the sequence of notes?</p>
  <ul>
    <li><strong>Type</strong>: Sequencing</li>
    <li><strong>Answers</strong>:
      <ul>
        <li>1️⃣ Do</li>
        <li>2️⃣ Re</li>
        <li>3️⃣ Mi</li>
        <li>4️⃣ Fa</li>
        <li>5️⃣ So</li>
        <li>6️⃣ La</li>
        <li>7️⃣ Ti</li>
      </ul>
    </li>
  </ul>
  <p><strong>Question</strong>: There are 2 correct answers, try to guess which options are correct:</p>
  <ul>
    <li><strong>Type</strong>: Multiple Response</li>
    <li><strong>Answers</strong>:
      <ul>
        <li>✅ Second option</li>
        <li>✅ Option one</li>
        <li>❌ This is the third option</li>
        <li>❌ And here is the fourth option</li>
      </ul>
    </li>
  </ul>
</details>

## Installation
<details>
  <summary>Click to expand</summary>
  <ol>
    <li><strong>Clone the Repository</strong>:
      <br>
      <a href="#" onclick="navigator.clipboard.writeText('git clone https://github.com/Radio125/SCORM-Test-Decoder-Telegram-Bot.git')">
        <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
      </a>
      <pre>git clone https://github.com/Radio125/SCORM-Test-Decoder-Telegram-Bot.git</pre>
    </li>
    <li><strong>Navigate to the Directory</strong>:
      <br>
      <a href="#" onclick="navigator.clipboard.writeText('cd SCORM-Test-Decoder-Telegram-Bot')">
        <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
      </a>
      <pre>cd SCORM-Test-Decoder-Telegram-Bot</pre>
    </li>
    <li><strong>Create a Virtual Environment (optional but recommended)</strong>:
      <br>
      <a href="#" onclick="navigator.clipboard.writeText('python -m venv venv')">
        <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
      </a>
      <pre>python -m venv venv</pre>
    </li>
    <li><strong>Activate the Virtual Environment</strong>:
      <ul>
        <li><strong>Windows</strong>:
          <br>
          <a href="#" onclick="navigator.clipboard.writeText('venv\\Scripts\\activate')">
            <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
          </a>
          <pre>venv\Scripts\activate</pre>
        </li>
        <li><strong>macOS/Linux</strong>:
          <br>
          <a href="#" onclick="navigator.clipboard.writeText('source venv/bin/activate')">
            <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
          </a>
          <pre>source venv/bin/activate</pre>
        </li>
      </ul>
    </li>
    <li><strong>Install Dependencies</strong>:
      <br>
      <a href="#" onclick="navigator.clipboard.writeText('pip install -r requirements.txt')">
        <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
      </a>
      <pre>pip install -r requirements.txt</pre>
    </li>
    <li><strong>Run the Bot</strong>:
      <br>
      <a href="#" onclick="navigator.clipboard.writeText('python bot.py')">
        <img alt="Copy to clipboard" src="https://img.shields.io/badge/copy%20command-1a73e8?logo=clipboard&style=flat-square">
      </a>
      <pre>python bot.py</pre>
    </li>
  </ol>
</details>

## Configuration
<details>
  <summary>Click to expand</summary>
  <p><strong>Bot Token</strong>: Replace the placeholder token in the <code>config.py</code> file with your actual Telegram Bot API token.</p>
  <p><strong>SCORM Files</strong>: Ensure SCORM JSON files are properly formatted for the bot to decode and process them effectively.</p>
</details>

## Contributing
<details>
  <summary>Click to expand</summary>
  <p>If you would like to contribute to the development of this bot, please feel free to fork the repository and submit pull requests. Any suggestions or bug reports are also welcome via GitHub issues.</p>
</details>

## Author
<details>
  <summary>Click to expand</summary>
  <p>Created by Radio125. Feel free to download, distribute, and modify the code. A simple like is enough!</p>
</details>

## License
<details>
  <summary>Click to expand</summary>
  <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
</details>
