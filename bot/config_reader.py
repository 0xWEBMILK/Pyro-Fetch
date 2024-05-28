from pydantic_settings import BaseSettings
from pydantic import SecretStr, BaseModel
from decouple import config



class BotSettings(BaseModel):
    api_hash: SecretStr = SecretStr(config('API_HASH'))
    api_id: SecretStr = SecretStr(config('API_ID'))

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'



bot_settings = BotSettings()