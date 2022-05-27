import asyncio
import os

from aiogram import Bot, Dispatcher, types, executor


from generator import gen_rythm

BOT_TOKEN = os.getenv('BOT_API_TOKEN')
PORT = int(os.environ.get('PORT', 80))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def default_message(message: types.Message):
    print(message)
    try:
        rythm_len = int(message.text)
    except ValueError:
        return await message.answer('Введите число, например 16')

    if rythm_len < 3:
        return await message.answer('Слишком маленький размер')
    rythm = gen_rythm(int(message.text))
    await message.answer(rythm)


async def on_startup(dp):
    await bot.set_webhook('https://didgen-app.herokuapp.com/')

if __name__ == '__main__':
    print('Bot started')

    loop = asyncio.get_event_loop()
    # executor.start_polling(dispatcher=dp, loop=loop)

    executor.start_webhook(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        webhook_path='',
        port=PORT,
        host='0.0.0.0'
    )
