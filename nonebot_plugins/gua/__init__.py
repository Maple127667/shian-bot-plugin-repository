from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata



from .config import Config

__plugin_meta__ = PluginMetadata(
    name="64gua",
    description="根据中国64卦制作的简易赛博迷信小插件",
    usage="使用指令：随机卦象，抽取一个卦象",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Maple127667/shian-bot-plugin-repository/tree/main/nonebot_plugins/gua",
    # 发布必填。

    # config=Config,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本 适配器功能）可不填写，否则应该列出插件支持的适配器。
)

config = get_plugin_config(Config)

import os
import random
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment,Message


qus1 = on_command("gua1",aliases={"随机卦象"},priority=1,block=True)

@qus1.handle()
async def _(matcher: Matcher, _: MessageEvent):
   
    ans_num = random.randint(1,64)
    ans1 = str(ans_num) + ".jpg"

    # 获取当前脚本的文件夹路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 拼接 img 文件夹下的 1.jpg 的路径
    img_path = os.path.join(current_dir, '64gua', ans1)

    # 存储路径到 path 变量
    path1 = img_path

    img = MessageSegment.image(file=path1)
    
    await matcher.send(img)

    # await matcher.send(str(path1))
    # await matcher.send(MessageSegment.image("./64gua/1.jpg"))
    await matcher.finish()
   