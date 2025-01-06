from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="asnwer",
    description="诗岸专用的一部分词库对应回复",
    usage="词库对应回复互动",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Maple127667/shian-bot-plugin-repository/tree/main/nonebot_plugins/answer",
    # 发布必填。

    # config=Config,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本 适配器功能）可不填写，否则应该列出插件支持的适配器。
)

config = get_plugin_config(Config)

#公开的山山词库，使用一般匹配模式和牌堆回复

#2024-10-1 update 由于ai回复引入，牌堆回复的一部分将会被废弃
#2024-12-30 update 由于ai回复增加了时间概念，废弃qus7 8 

import random
from nonebot import on_command
#from nonebot import on_regex
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent

qus1 = on_command("ans1",aliases={"山山在吗","诗岸在吗"},priority=5,block=True)

qus2 = on_command("ans2",aliases={"山山老婆","诗岸老婆"},priority=5,block=True) 

qus3 = on_command("ans3",aliases={"山山骂他","山山骂她","诗岸骂她","诗岸骂他"},priority=5,block=True) 

qus4 = on_command("ans4",aliases={"山山可爱","诗岸可爱"},priority=5,block=True) 

qus5 = on_command("ans5",aliases={"山山你好","诗岸你好"},priority=5,block=True) 

# qus6 = on_regex(".*山山.*|.*诗岸.*",priority=20)

#qus7 = on_command("ans7",aliases={"山山现在几点了","诗岸现在几点了"},block=True) 

#qus8 = on_command("ans8",aliases={"山山今天几号","诗岸今天几号"},block=True) 

# qus9 = on_regex("^早$|早安|山山早|诗岸早|早上好|早~",priority=2)

# qus10 = on_regex("晚安|睡了",priority=2)

@qus1.handle()
async def _(matcher: Matcher, _: MessageEvent):
    ans_tup = (
        "关注诗岸喵，关注诗岸谢谢喵",
        "在！有何吩咐！",
        "唔...找山山有什么事呢？",
        "早上好！...诶诶，是早上吗？最近熬夜忘了时间啦",
        "（吹灭火器）",
        "（从米缸钻出来.jpg)"
    )

    ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
    await matcher.finish(ans1)

@qus2.handle()
async def _(matcher: Matcher, _: MessageEvent):
    ans_tup = (
        "我才不是你老婆，你可不要瞎说！",
"肥宅不要乱叫人老婆啊！",
"你一定是认错人了",
"才不是呢！（锤）"
    )

    ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
    await matcher.finish(ans1)

@qus3.handle()
async def _(matcher: Matcher, _: MessageEvent):
    ans_tup = (
        "喂喂！你是笨蛋嘛？（歪头）",
"你好笨哦（锤）",
"你能不能聪明一点呀！（微恼）"
    )

    ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
    await matcher.finish(ans1)

@qus4.handle()
async def _(matcher: Matcher, _: MessageEvent):
    ans_tup = (
       "这样的夸奖有点突然呢（捂脸）",
"谢谢夸奖啦www",
"欸..是在夸我吗，总..总之是感谢啦（逃开）"
    )

    ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
    await matcher.finish(ans1)

@qus5.handle()
async def _(matcher: Matcher, _: MessageEvent):
    ans_tup = (
      "你好哟~这里是诗岸desu",
"山山在哟~想山山了吗？",
"现在该说什么安呢？（思索) 那就早中晚都好吧~" )

    ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
    await matcher.finish(ans1)

# @qus6.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     ans_tup = (
#       "山山在哦~",
# "在哦在哦~有什么事~",
# "（吹灭火器ing）" )
#     if((random.randint(0,10))<=2):
#         ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
#         await matcher.finish(ans1)
#     else:
#         await matcher.finish()
    

# @qus7.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     t=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     t="现在是"+t+"咯！记得注意身体健康哟，按时休息！"
#     await matcher.finish(t)

# @qus8.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     t=str(time.strftime("%Y-%m-%d", time.localtime()))
#     t="今天是"+t+"！祝今日好运连连~！"
#     await matcher.finish(t)

# @qus9.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     ans_tup = ("早呀~",
#                "早早早！",
#                "今天又是阳光明媚的一天呢~",
#                "（揉眼睛ing）",
#                "早~（睡眼惺忪）",
#                "早呀~今天又是开心的一天"
#                "早上好呢！"
#        )

#     ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
#     await matcher.finish(ans1)

# @qus10.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     #早上5-8点 5-8
#     ans1_tup = ("现在可不是晚安的时间呐...你不会到现在还没睡吧？（担心）快去睡哦","唔？居然是这个时间道晚安吗？已经很晚了哦，晚安")
#     #凌晨2-5点
#     ans2_tup = ("已经很晚很晚咯，祝好梦呀","熬夜很伤身体的（担心）快睡吧？")
#     #正常晚上9-12点
#     ans3_tup = ("晚安，诗岸会为您祈愿今日的好梦","晚安，诗岸会为您祈愿今日的好梦","晚安，祝您做个好梦","晚安，今日已经很努力了呢，好好休息吧")
#     #早上8点-晚上9点前
#     ans4_tup = ("呐呐，现在不是说晚安的时间吧（歪头）","啊嘞？现在晚安嘛？")

#     ans_tup = ()

#     t = time.localtime()
#     hour = t.tm_hour
#     if(hour >= 5 and hour < 8): #测试完毕
#         ans_tup = ans1_tup
#     elif (hour >= 2 and hour < 5):#测试完毕
#         ans_tup = ans2_tup
#     elif((hour >= 21 and hour < 24) or (hour >= 0 and hour < 2) ): #测试完毕
#         ans_tup = ans3_tup
#     else:                           #debug一次（恼 8-3
#         ans_tup = ans4_tup
    
#     ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
#     await matcher.finish(ans1)  









#qus1 = on_command("ans_",aliases={"山山在吗","诗岸在吗"},block=True)

# @qus_.handle()
# async def _(matcher: Matcher, _: MessageEvent):
#     ans_tup = (
#        )
#     ans1=ans_tup[random.randint(0,len(ans_tup)-1)]
#     await matcher.finish(ans1)