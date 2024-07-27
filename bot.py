import cataas, config
import asyncio, logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
file_handler = logging.FileHandler('logs\log.log', mode='a')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s'))
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s'))
 
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('Bot has been laucnhed.')


bot = Bot(config.TG_BOT_TOKEN)

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
	await message.answer('Приветики :3\nЭтот бот может отправлять картинки с котиками! (=^･^=)\nНапиши /help чтобы узнать больше. ;3')

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
	await message.answer('Информация о командах (=^-ω-^=)\n\n/cat: картинка с рандомным котиком\n\n/gif: гифка с рандомным котиком\n\n/tag <tag1> <tag2> <tag...>: картинка с котиком, соответствующая заданным тэгам')

@dp.message(Command('cat'))
async def cmd_cat(message: types.Message):
	await bot.send_chat_action(message.chat.id, 'upload_photo')
	cat = cataas.get_cat()
	await bot.send_photo(chat_id=message.chat.id, photo=cat)

	logger.info(f"[chat_id: {message.chat.id, message.chat.first_name, message.chat.last_name,}] - [action: cat] - [url: {cat}]")

@dp.message(Command('gif'))
async def cmd_gif(message: types.Message):
	await bot.send_chat_action(message.chat.id, 'upload_video')
	gif = cataas.get_gif()
	await bot.send_video(message.chat.id, gif)

	logger.info(f"[chat_id: {message.chat.id, message.chat.first_name, message.chat.last_name,}] - [action: gif] - [url: {gif}]")

@dp.message(Command('tag'))
async def cmd_gif(message: types.Message):
	await bot.send_chat_action(message.chat.id, 'upload_video')
	str = (message.text).replace('/tag', '').strip().replace(' ', ',')
	tag = cataas.get_tag(str)

	try:
		await bot.send_video(message.chat.id, tag)

		logger.info(f"[chat_id: {message.chat.id, message.chat.first_name, message.chat.last_name,}] - [action: tag] - [message: {message.text}] - [url: {tag}]")
	except:
		logger.info(f"[chat_id: {message.chat.id, message.chat.first_name, message.chat.last_name,}] - [ERROR: InvalidTag] - [message: {message.text}]")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

# TODO: сделать Inline режим (вызов через клаву в чатах)