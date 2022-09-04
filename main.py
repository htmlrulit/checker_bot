import asyncio
import random
import vk_api
import vk
from vkbottle.bot import Bot, Message
from vkbottle import API
import os
randint_low = 0
randint_high = 2000000000
from vkbottle import Keyboard, KeyboardButtonColor, Text
keyboard = Keyboard(one_time=True, inline=False)
keyboard.add(Text("Проверить статус ботов"), color=KeyboardButtonColor.POSITIVE)
adminID = 158348140
bot = Bot(token="main_token")
api = API("main_token")
token_1 = "token_1"
token_2 = "token_2"
token_3 = "token_3"
token_4 = "token_4"
token_5 = "token_5"
token_6 = "token_6"
@bot.on.message(text=["check", "Проверить статус ботов"])
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f"ok", keyboard=keyboard.get_json())
    await api.messages.send(access_token=token_1, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))
    await api.messages.send(access_token=token_2, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))
    await api.messages.send(access_token=token_3, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))
    await api.messages.send(access_token=token_4, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))
    await api.messages.send(access_token=token_5, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))
    await api.messages.send(access_token=token_6, user_id=adminID, peer_id=adminID, message="✅ Бот сообщества работает корректно", random_id=(random.randint(randint_low, randint_high)))




    
bot.run_forever()