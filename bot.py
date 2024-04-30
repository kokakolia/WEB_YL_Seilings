import os

from telegram._bot import Bot

import logging
import asyncio
from dotenv import load_dotenv

load_dotenv('.env')

bot_token = os.getenv('BOT_TOKEN')

chat_id = '842504537'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def send_message(text):
    bot = Bot(token=bot_token)

    await bot.send_message(chat_id=chat_id, text=text)


# Пример использования функции
def bot_send_order(width, length, material, lamps, color):
    text = f'Ширина: {width}\nДлина {length}\nКоличество ламп: {lamps}\nМатериал:{material}\nЦвет:{color}'
    asyncio.run(send_message(text))
