from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata



from .config import Config

__plugin_meta__ = PluginMetadata(
    name="gua",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

import os
import random
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment,Message


qus1 = on_command("gua1",aliases={"随机卦象"},block=True)

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
   