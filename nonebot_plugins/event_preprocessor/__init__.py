from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="run_preprocessor",
    description="关于nonebot端与sealdice端兼容的bot休眠功能（不完善）",
    usage="同sealdice、溯洄等骰娘的休眠方式",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Maple127667/shian-bot-plugin-repository/tree/main/nonebot_plugins/run_preprocessor",
    # 发布必填。

    # config=Config,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本 适配器功能）可不填写，否则应该列出插件支持的适配器。
)

config = get_plugin_config(Config)

from nonebot.adapters.onebot.v11 import GroupMessageEvent,GROUP_ADMIN,GROUP_OWNER,Message,Bot
from nonebot.params import CommandArg
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.message import run_preprocessor
from nonebot.exception import IgnoredException
import json
import re

qus1 = on_command("ans_",aliases={"。bot off",".bot off"},priority=0,permission = SUPERUSER | GROUP_ADMIN | GROUP_OWNER,block=True)
qus2 = on_command("ans_",aliases={"。bot on" ,".bot on" },priority=0,permission = SUPERUSER | GROUP_ADMIN | GROUP_OWNER,block=True)


@qus1.handle()
async def _(matcher: Matcher, _: GroupMessageEvent,args: Message = CommandArg()):
    botid = args.extract_plain_text()
    if (botid != "3070079089" and botid != ""):
        await matcher.finish()

    path = 'shian/plugins/event_preprocessor/blacklist' + '.json'
    groupid = int(_.group_id)

    try:
        with open(path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    values = data.values()

    values = str(values)[14:-3]

    values = values.replace(" '",'')
    values = values.replace("'",'')
    values_list = values.split(',')
    
    values_list = [ int(x) for x in values_list ]

    # await matcher.send(str(values_list))


    if groupid not in values_list:
        values_list.append(groupid)
    
    for i in range(0,len(values_list)-1):
        if values_list[i]  == '' :
            del values_list[i]


    data = {"blacklist":str(values_list)[1:-1]}

    with open(path, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)

    await matcher.finish("睡觉去咯")

@qus2.handle()
async def _(matcher: Matcher, _: GroupMessageEvent,args: Message = CommandArg()):
    botid = args.extract_plain_text()
    if (botid != "3070079089" and botid != ""):
        await matcher.finish()

    path = 'shian/plugins/event_preprocessor/blacklist' + '.json'
    groupid = int(_.group_id)

    try:
        with open(path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    values = data.values()

    values = str(values)[14:-3]

    values = values.replace(" '",'')
    values = values.replace("'",'')
    values_list = values.split(',')

    values_list = [ int(x) for x in values_list ]

    # await matcher.send(str(values_list))
    # await matcher.send(str(groupid))

    for i in range(0,len(values_list)):
        if values_list[i]  ==  groupid :
            # await matcher.send("compare"+str(values_list[i]))
            # await matcher.send("ping")
            del values_list[i]

    for i in range(0,len(values_list)):
        if values_list[i]  == '' :
            del values_list[i]


    data = {"blacklist":str(values_list)[1:-1]}

    with open(path, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)

    await matcher.finish("又要干活吗（")


@run_preprocessor
async def do_something(Bot:Bot,_:GroupMessageEvent):
    text = str(_.get_message())
    path = 'shian/plugins/event_preprocessor/blacklist' + '.json'
    if re.search("on",text) is None:
        
        try:
            with open(path, 'r',encoding='utf-8') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        values = data.values()

        values = str(values)[14:-3]

        values = values.replace(" '",'')
        values = values.replace("'",'')
        values_list = values.split(',')

        values_list = [ int(x) for x in values_list ]

        if int(_.group_id) in values_list:
            # await Bot.send_private_msg(user_id= "1276679255" , message= str(text))
            raise IgnoredException("")



