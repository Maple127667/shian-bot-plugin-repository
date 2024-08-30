from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="gugu_no",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

from nonebot import require

require("nonebot_plugin_apscheduler")

import time
from nonebot import on_command
from nonebot import on_regex
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot_plugin_apscheduler import scheduler
from apscheduler.schedulers.background import BackgroundScheduler

qus = on_command("山山提醒大家开团啦",block=True)

timing = scheduler


@qus.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    name = args.extract_plain_text()
    scheduler = BackgroundScheduler()
    scheduler.add_job(name, 'date', run_date=date(2017, 12, 13), args=['text'])
