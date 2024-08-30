from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="collections",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)


from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent

import json



qus = on_command("ans_",aliases={"查询歌词收藏夹"},block=True)


@qus.handle()
async def _(matcher: Matcher, _: MessageEvent):

    path = 'data/music_collections/' + str(_.user_id) + '.json'

    try:
        with open(path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
        await matcher.finish("你还没有收集歌词哦？\n快去 .今日运势 抽一个吧")

    values = data.values()

    values = str(values)[14:-3]

    values = values.replace(" '",'')
    values = values.replace("'",'')
    values_list = values.split(',')
    
    ans = ''

    for i in range(0,len(values_list)-1):
        if values_list[i]  == '' :
            del values_list[i]
    
    for i in values_list:
        ans = ans + "\"" + i +'\"\n'
    
    ans = ans + "已经收集" + str(len(values_list)) + "/52"

    await matcher.finish(ans)