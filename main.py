import asyncio
import os
from collections import defaultdict

from aiogram import Bot, Dispatcher, types, executor


from generator import gen_rythm

BOT_TOKEN = os.getenv('BOT_API_TOKEN')
PORT = int(os.environ.get('PORT', 80))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

googlesheet_id = '1fika6X6aCOBhUV882FoS897QrXmtSkxOdCQvrEXYitI'

stages = defaultdict(int)
names = [['Саша', 'Женя', 'Крутов', 'Ангелина', 'Катя', 'Отмена']]
chosen_name = {}
chosen_sheet = {}


@dp.message_handler()
async def default_message(message: types.Message):
    print(message)
    rythm = gen_rythm(int(message.text))
    await message.answer(rythm)


if __name__ == '__main__':
    print('Bot started')

    loop = asyncio.get_event_loop()
    # executor.start_polling(dispatcher=dp, loop=loop)

    executor.start_webhook(
        dispatcher=dp,
        skip_updates=True,
        webhook_path='',
        port=PORT,
        host='0.0.0.0'
    )
