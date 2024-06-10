import json
import logging
import os
import tempfile
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import asyncio

logging.basicConfig(level=logging.DEBUG)

# Токен бота и инициализация
from config import TOKEN
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Функция для парсинга текста из частей
def parse_text_parts(text_parts):
    return ''.join([part['t'] for part in text_parts])

# Функция для декодирования парного вопроса
def decode_matching_question(data):
    pairs = []
    ms_data = data.get('c', {}).get('ms', {}).get('b', {})
    order = data.get('c', {}).get('ms', {}).get('o', [])

    for key in order:
        if key in ms_data:
            pair_data = ms_data[key]
            left_text = parse_text_parts(pair_data['l']['t']['b']['B'][list(pair_data['l']['t']['b']['B'].keys())[0]]['c'])
            right_text = parse_text_parts(pair_data['r']['t']['b']['B'][list(pair_data['r']['t']['b']['B'].keys())[0]]['c'])
            pairs.append((left_text, right_text))
    
    return pairs

# Функция для декодирования вопросов и ответов
def decode_questions(json_data):
    questions = []
    question_types = {
        'mt': 'Matching',         # Сопоставление
        'mc': 'Multiple Choice',  # Множественный выбор
        'ti': 'Text Input',       # Ввод текста
        'sq': 'Sequencing',       # Sequencing
        'mr': 'Multiple Response' # Множественные ответы
    }

    for qid, qdata in json_data['state'].get('q', {}).get('B', {}).items():
        question = {}
        question['id'] = qid
        question['type'] = question_types.get(qdata.get('t'), 'Unknown')  # Определение типа вопроса

        # Получение текста вопроса
        question_text_parts = qdata.get('d', {}).get('b', {}).get('B', {})
        if question_text_parts:
            question['text'] = parse_text_parts(question_text_parts[list(question_text_parts.keys())[0]]['c'])
        else:
            question['text'] = 'Не удалось распознать текст вопроса'

        # Обработка ответов в зависимости от типа вопроса
        question['answers'] = []

        if question['type'] == 'Matching':
            pairs = decode_matching_question(qdata)
            question['answers'] = [f"{left} -> {right}" for left, right in pairs]

        elif question['type'] == 'Sequencing':
            # Извлекаем ключи для правильной последовательности
            sequence_order = qdata.get('c', {}).get('o', [])
            if not sequence_order:
                sequence_order = sorted(qdata.get('c', {}).get('B', {}).keys())

            # Сортируем ответы по ключам
            for key in sequence_order:
                answer_data = qdata.get('c', {}).get('B', {}).get(key, {})
                answer_text_parts = answer_data.get('t', {}).get('b', {}).get('B', {})
                if answer_text_parts:
                    answer_text = parse_text_parts(answer_text_parts[list(answer_text_parts.keys())[0]]['c'])
                else:
                    answer_text = 'Не удалось распознать текст ответа'
                question['answers'].append({
                    'text': answer_text,
                    'order': len(question['answers']) + 1  # Нумерация для последовательности
                })

        else:
            for aid, adata in qdata.get('c', {}).get('B', {}).items():
                answer_text_parts = adata.get('t', {}).get('b', {}).get('B', {})
                if answer_text_parts:
                    answer_text = parse_text_parts(answer_text_parts[list(answer_text_parts.keys())[0]]['c'])
                else:
                    answer_text = 'Не удалось распознать текст ответа'
                
                answer = {
                    'text': answer_text,
                    'correct': adata.get('c', False)  # Определение правильного ответа
                }
                question['answers'].append(answer)

        questions.append(question)

    return questions

# Функция для отправки сообщений частями
async def send_message_in_parts(chat_id, text, max_length=4096):
    if len(text) <= max_length:
        await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)
    else:
        parts = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        for part in parts:
            await bot.send_message(chat_id, part, parse_mode=ParseMode.HTML)

import html

def format_questions(questions):
    emoji_numbers = {
        1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣",
        6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣", 10: "🔟",
        11: "1️⃣1️⃣", 12: "1️⃣2️⃣", 13: "1️⃣3️⃣", 14: "1️⃣4️⃣", 15: "1️⃣5️⃣",
        16: "1️⃣6️⃣", 17: "1️⃣7️⃣", 18: "1️⃣8️⃣", 19: "1️⃣9️⃣", 20: "2️⃣0️⃣"
    }

    formatted = ""
    for question in questions:
        # Экранируем текст вопроса
        question_text = html.escape(question['text'])
        formatted += f"<b>Вопрос:</b> {question_text}\nТип: {question['type']}\n<b>Ответы:</b>\n"
        
        if question['type'] == 'Matching':
            for pair in question['answers']:
                # Экранируем текст парных ответов
                formatted += f"🔗 {html.escape(pair)}\n"
        elif question['type'] == 'Sequencing':
            for answer in sorted(question['answers'], key=lambda x: x['order']):
                number_emoji = emoji_numbers.get(answer['order'], f"{answer['order']}️⃣")
                # Экранируем текст ответа
                formatted += f"{number_emoji} {html.escape(answer['text'])}\n"
        else:
            for answer in question['answers']:
                correct_marker = "✅" if answer['correct'] else "❌"
                # Экранируем текст ответа
                formatted += f"{correct_marker} {html.escape(answer['text'])}\n"
        formatted += "\n"

    return formatted


# Обработчик команды start
@dp.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    russian_message = await message.answer(
        "Привет! 🌟\n\n"
        "Спасибо, что обратились к боту для расшифровки теста SCORM! Я готов помочь. Для начала, отправьте мне JSON файл с тестом. Если у вас архив ZIP, нам пока нужен только файл data-1.json из папки res. 📂\n\n"
        "Вот шаги, которые нужно выполнить:\n"
        "1️⃣ Скачайте SCORM 1.2 или 2004.\n"
        "2️⃣ Распакуйте полученный ZIP архив.\n"
        "3️⃣ Откройте папку и найдите папку res.\n"
        "4️⃣ Внутри res найдите файл data-1.json (не забудьте, что расширение .json может быть не видно в простом названии файла).\n"
        "5️⃣ Отправьте этот файл мне, и я сделаю всю работу по расшифровке для вас! 🤖\n\n"
        "Если у вас возникнут вопросы или нужна помощь, не стесняйтесь спрашивать. Удачи! 💪"
    )
    english_message = await message.answer(
        "Hello! 🌟\n\n"
        "Thank you for reaching out to the bot for decrypting the SCORM test! I'm ready to help. To start, please send me a JSON file with the test. If you have a ZIP archive, for now we only need the data-1.json file from the res folder. 📂\n\n"
        "Here are the steps to follow:\n"
        "1️⃣ Download SCORM 1.2 or 2004.\n"
        "2️⃣ Unpack the received ZIP archive.\n"
        "3️⃣ Open the folder and find the res folder.\n"
        "4️⃣ Inside res, find the data-1.json file (remember that the .json extension may not be visible in the simple file name).\n"
        "5️⃣ Send me this file, and I will do all the decryption work for you! 🤖\n\n"
        "If you have any questions or need help, feel free to ask. Good luck! 💪"
    )
    await asyncio.sleep(60)
    await russian_message.delete()
    await english_message.delete()

# Обработчик для обработки JSON файла
@dp.message(lambda message: message.document and message.document.file_name.endswith('.json'))
async def file_handler(message: types.Message, state: FSMContext):
    logging.info(f"Получен файл от пользователя {message.from_user.id}")
    
    try:
        # Получение файла
        file_info = await bot.get_file(message.document.file_id)
        file_data = await bot.download_file(file_info.file_path)
        
        temp_file_path = tempfile.mktemp()
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(file_data.read())

        logging.debug(f"Файл сохранен временно: {temp_file_path}")

        # Декодирование JSON файла
        with open(temp_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        logging.debug("JSON файл успешно загружен")

        questions = decode_questions(json_data)
        logging.debug("Начало декодирования вопросов")

        formatted_questions = format_questions(questions)
        logging.debug("Завершение декодирования вопросов")

        await send_message_in_parts(message.chat.id, formatted_questions, max_length=4096)
        logging.info("Вопросы успешно отправлены пользователю")

        # Удаление временного файла
        os.remove(temp_file_path)

    except Exception as e:
        logging.error(f"Ошибка при обработке файла: {e}")
        await message.answer(f"Произошла ошибка при обработке файла: {e}")

# Запуск polling
if __name__ == "__main__":
    dp.run_polling(bot)
