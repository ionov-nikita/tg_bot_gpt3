import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import BotState
from . import text_messages as texts
from .utils import gpt

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    fullname = message.from_user.first_name
    await message.answer(text=texts.START_COMMAND_TEXT.format(fullname=fullname))
    await state.set_state(state=BotState.main_state)


@router.message(Command("help"))
async def help_command(message: types.Message, state: FSMContext):
    await message.answer(text=texts.HELP_COMMAND_TEXT)
    await state.set_state(state=BotState.main_state)


@router.message()
async def echo_to_user(message: types.Message, state: FSMContext):
    prompt, result = message.text, None
    await message.bot.send_chat_action(chat_id=message.from_user.id, action="typing")
    try:
        result = await gpt.get_answer(prompt=prompt)
    except Exception as error:
        logger.exception("Could execute user's prompt: %s", error)

    if result:
        await message.reply(text=result)
    else:
        await message.answer(text=texts.BOT_ERROR_TEXT)

    await state.set_state(state=BotState.main_state)
