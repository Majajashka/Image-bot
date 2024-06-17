import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from app.core.service.user import get_or_create_user
from app.infrastructure.database.holder import HolderRepo

router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner, repo: HolderRepo):
    await message.answer(i18n.start(name=message.from_user.first_name))
    await get_or_create_user(message.from_user.id, repo.users)

