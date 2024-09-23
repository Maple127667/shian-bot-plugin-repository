# from nonebot import get_plugin_config
# from nonebot.plugin import PluginMetadata

# from .config import Config

# __plugin_meta__ = PluginMetadata(
#     name="answer",
#     description="",
#     usage="",
#     config=Config,
# )

# config = get_plugin_config(Config)

# #公开的山山词库，使用一般匹配模式和牌堆回复

# import random
# import time
# from nonebot import on_command
# from nonebot import on_regex
# from nonebot.matcher import Matcher
# from nonebot.adapters.onebot.v11 import MessageEvent



# qus1 = on_command("ans_",aliases={"转动轮盘"},block=True)

# @qus1.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     ans_tup = (
#        )
#     ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
#     await matcher.finish(ans1)