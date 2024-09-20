from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="russian_ban",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)


import random
import json
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,GroupRequestEvent
from nonebot.adapters import Message
from nonebot.params import CommandArg



qus1 = on_command("ans_",aliases={"填入子弹","填充子弹"},block=True) #开始填入子弹
qus2 = on_command("ans_",aliases={"开枪"},block=True)
qus3 = on_command("ans_",aliases={"转动轮盘"},block=True)

ans_alive = []
ans_dead = []
flag = 0

@qus1.handle()
async def _(matcher: Matcher, _: GroupMessageEvent,args: Message = CommandArg()):
    num = args.extract_plain_text()
    if num.isdigit() and (int(num)>= 0 and int(num)<=6) :
        num = int(num)
        list = random.sample(range(0,6), num)
    else:
        await matcher.finish("请输入正确的子弹数目")

    russian_list = [0,0,0,0,0,0]
    for i in list:
        russian_list[i] = 1

    path = 'data/russian_ban/' + str(_.group_id) + '.json'

    data = {"russian" : str(russian_list)[1:-1]}

    with open(path, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)
    global ans_alive,ans_dead,flag
    flag = 0
    ans_alive = []
    ans_dead = []
    await matcher.finish("子弹装填完毕")

@qus2.handle()
async def _(Bot : Bot ,matcher: Matcher, _: GroupMessageEvent,args: Message = CommandArg()):
    global flag
    if(flag == -1):
        flag = 0
        await matcher.finish("上一轮已经结束，请填入子弹开启下一轮")
    path = 'data/russian_ban/' + str(_.group_id) + '.json'
    global ans_alive,ans_dead

    try:
        with open(path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    values = data.values()
    if not values:
        await matcher.finish("还没有可用的轮盘,请先转动轮盘来填充子弹")
    values = str(values)[14:-3]
    values = values.replace(", ",',')
    values_list = values.split(',')
    values_list = [ int(x) for x in values_list ]

    nickname = _.sender.nickname
    # await matcher.send(str(nickname))


    # await matcher.send(str(values_list))

    if values_list[0]:
        wujing  = random.randint(0,20)#你能反应子弹
        if wujing:
            ans1_tup = ("pong!你死了..",
                    "随着一声枪响，你的意识逐渐模糊.."
                    "嘭..你似乎能听到子弹穿过你的颅骨，但是你已经没机会细想了",
                    "砰...死神在嘲笑你",
                    "砰...呵,愚蠢的死法"
            )
            if nickname not in ans_dead:
                ans_dead.append(nickname)
            ans=ans1_tup[random.randint(0,len(ans1_tup)-1)]
            # await matcher.send(ans1)
            await Bot.set_group_ban(group_id=_.group_id , user_id=_.user_id ,duration= 60)
        else:
            ans2_tup = ("pong!子弹从你的耳边划过，你在子弹发射的一瞬间躲过了子弹..你可以嘲笑死神了",
            "咔哒..子弹撞到了底火上，但是这意外的是一颗哑弹，幸运女神保佑你"
            )
            ans=ans2_tup[random.randint(0,len(ans2_tup)-1)]

            if nickname not in ans_alive:
                ans_alive.append(nickname)
            # await matcher.send(ans2)
        # await bot.set_group_ban(group_id=group,user_id=qq,duration=sj)
        del values_list[0]
        values_list.append(0)
    else:
        ans3_tup = ("咔哒..什么都没有发生",
                    "咔哒...至少这次你是幸运的",
                    "什么都没有发生.."
            )
        if nickname not in ans_alive:
                ans_alive.append(nickname)
        ans=ans3_tup[random.randint(0,len(ans3_tup)-1)]
        # await matcher.send(ans3)
        del values_list[0]
        values_list.append(0)

    data = {"russian":str(values_list)[1:-1]}
    with open(path, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)

    ans_alive = list(set(ans_alive)-set(ans_dead))

    flag = 0
    for i in values_list:
        if(i == 1):
            flag += 1
    if flag == 0 :
        ans_alive_str = str(ans_alive)[1:-1]
        ans_dead_str = str(ans_dead)[1:-1]
        
        ans_alive_str = ans_alive_str.replace("'","")
        ans_dead_str =ans_dead_str.replace("'","")

        await matcher.send(ans+"\n弹仓已空\n存活名单："+ans_alive_str+"\n死亡名单："+ans_dead_str)
        ans_alive = []
        ans_dead = []
        flag = -1
    else:
        await matcher.send(ans+"\n还有"+str(flag)+"发子弹")
    await matcher.finish()

@qus3.handle()
async def _(Bot : Bot ,matcher: Matcher, _: GroupMessageEvent,args: Message = CommandArg()):

    path = 'data/russian_ban/' + str(_.group_id) + '.json'

    try:
        with open(path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    values = data.values()
    if not values:
        await matcher.finish("还没有可用的轮盘,请先转动轮盘来填充子弹")
    values = str(values)[14:-3]

    # await matcher.send(str(values) )
    values = values.replace(", ",',')
    # await matcher.send(str(values))

    values_list = values.split(',')

    # await matcher.send(str(values_list))

    values_list = [ int(x) for x in values_list ]

    # await matcher.send(str(values_list))

    for i in range(0,random.randint(0,6)):
        temp = values_list[0]
        del values_list[0]
        values_list.append(temp)

    data = {"russian":str(values_list)[1:-1]}
    with open(path, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4,ensure_ascii=False)

    await matcher.finish("弹仓旋转后随着咔哒一声，停了下来")