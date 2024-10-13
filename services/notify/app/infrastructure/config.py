import os
from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    model_config = ConfigDict(extra='ignore')

    ENV: str = "local"
    BOT_TOKEN: str
    CONSUME_TOPIC: str
    KAFKA_BOOTSTRAP_SERVERS: str


class LocalConfig(Config):
    pass


def get_config(_env_file):
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(_env_file=_env_file)
    }
    return config_type[env]


config: Config = get_config(_env_file=os.path.join(Path(__file__).parents[1], ".env"))