from pydantic import BaseSettings


class BotApiSettings(BaseSettings):
    token: str

    class Config:
        env_prefix: str = 'BOT_API_'
