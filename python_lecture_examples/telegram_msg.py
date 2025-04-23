from telegram import Bot

api_key = ''
chat_id = ''

telebot = Bot(token=api_key)  # 텔레그램 봇 초기화
telebot.send_message(chat_id=chat_id, text="샘플 메시지 전송!", timeout=3)