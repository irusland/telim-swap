import abc

from aiogram import types


class BaseHandler(abc.ABC):
    @abc.abstractmethod
    async def __call__(self, message: types.Message) -> None:
        pass
