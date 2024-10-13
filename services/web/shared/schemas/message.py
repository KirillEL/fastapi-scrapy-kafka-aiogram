from pydantic import BaseModel, ConfigDict, Field


class MessageCreateDto(BaseModel):
    model_config = ConfigDict(extra='forbid')

    currency_char_code: str
    telegram_id: int = Field(gt=0)
