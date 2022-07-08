from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.webhook import configure_app
from aiogram.utils.executor import start_webhook, set_webhook
from aiohttp import web
import logging
import os


API_TOKEN = "5162165790:AAHD_2v5tB5hntJY9S0Gy-mtnAIrFc--uSg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


routes = web.RouteTableDef()


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("start!")


async def on_startup(dispatcher):
    await bot.set_webhook('https://monobank-webhook.herokuapp.com/bot', drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@routes.post('/post')
async def api_handler(request):
    await bot.send_message(chat_id=389471081, text='test')
    return web.json_response({"status": "OK"}, status=200)


app = web.Application()
# add a custom route
app.add_routes(routes)
# every request to /bot route will be retransmitted to dispatcher to be handled
# as a bot update
configure_app(dp, app, "/bot")

on_shutdown(dp)
on_startup(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app, port=os.getenv('PORT', 9000))
'''    
    executor = set_webhook(dispatcher=dp,
                           webhook_path='/bot',
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           route_name='bot',
                           web_app=app)
'''

