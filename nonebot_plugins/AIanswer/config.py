from pydantic import BaseModel
import nonebot


config = nonebot.get_driver().config


class Config(BaseModel):
    """Plugin Config Here"""
    SUPERUSER:str = config.superusers
    # DEEPSEEK_API:str ="sk-c5PIxkThZRA3zySGB723A26972D44dC0BfFe20A9506151Df" #填写自己的deepseek中的api