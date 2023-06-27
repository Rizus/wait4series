from pydantic import BaseSettings, SecretStr
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ADMIN_ID: int
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_IP: str
    DATABASE_PORT: int
    DATABASE_TIMEOUT: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


# При импорте файла сразу создастся
# и провалидируется объект конфига,
# который можно далее импортировать из разных мест
config = Settings()
