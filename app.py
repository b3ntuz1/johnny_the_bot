from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from settings import TOKEN

from models import Person
import chat_member
import wtf

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)
top_ten = []


@dp.message_handler()
async def main types.Message):
    ''' потрібно щоб менше тривожити бд '''
    if msg.from_user.id not in top_ten:
        top_ten.insert(0, chat_member.get_user(msg.from_user))

        if len(top_ten) == 10:
            top_ten.pop()
    
    await msg.reply(str(top_ten))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply('Hello\. Im bot\. Its a test message')


@dp.message_handler(commands=wtf.wtf_varians)
async def wtf_cmd(msg: types.Message):
    user_id =  msg.from_user.id
    if chat_member.is_admin(msg.chat, user_id):
        await msg.answer("I can not mute administrators")
        return 0

    time_in_secs = wtf.wtf_main()
    # old version
    # await msg.chat.restrict(user_id, until_date=time_in_secs[0])
    #
    # new version
    chat_member.mute(msg.chat, user_id, time_in_secs[0])

    await msg.answer(
        f'__{msg.from_user.first_name}__  muted for {time_in_secs[1]}'
        )


if __name__ == '__main__':
    executor.start_polling(dp)

