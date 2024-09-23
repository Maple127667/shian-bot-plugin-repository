from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="fortune",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)


import random
import math
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageEvent

from datetime import datetime


qus = on_command("。山山今日运势是什么呀",aliases={"。山山今日运势","。诗岸今日运势","。。今日运势","。.今日运势"},block=True)



@qus.handle()
async def _(matcher: Matcher, _: MessageEvent):
    
    # 获取当前日期和时间
    now = datetime.now()

    # 提取年、月、日
    year = now.year
    month = now.month
    day = now.day

    # 组合成整数形式
    date_int = year * 10000 + month * 100 + day


    seed = _.user_id + date_int
    random.seed(seed)
    output1 = random.randint(1,100)
    output2 = random.randint(1,100)
    output3 = random.randint(1,100)


    output1 = math.ceil(math.log((((output1/33.3)+1)),2)*49.9725)
    output2 = math.ceil(math.log((((output2/33.3)+1)),2)*49.9725)
    output3 = math.ceil(math.log((((output3/33.3)+1)),2)*49.9725)



    # seed = _.user_id
    # output4 = (output1 + output2 + output3)/3 + random.randint(-20,20)
    # if output4 < 0 :
    #     output4 = 0
    # elif output4 >100:
    #     output4 = 100



    dianping = ''
    music_dianping = ''
    seed = _.user_id + date_int

    music_tup1 = (        #大吉
            "你是所有漫反射的光线而我简出你身影",
            "深净的蓝色天空一切明丽得悲恸",
            "就这样吧所有的杂七杂八胡思乱想推给明天",
            "夜卷揉白墨 返照于云色",
            "说道揽望流风 有静美晴空 只怕一伫如梦 一瞬即永恒",
            "很期待 雪山脚下 约谁稍作停顿 欣赏那的 瑰丽星辰",
            "很期待 幻光花中 对谁念念咒文 看看会有 什么发生",
            "青春从来不是为人生草稿 也许答案只有自己知晓",
            "温暖阳光在此刻照到我的空白心脏",
            "快来将我戳破 柔软情绪快把我淹没",
            "愿这悠长岁月温和待你左右",
            "明灭繁星 忽远忽近 星光晶莹 如影随形",
            "如同星空一般完美画面 在这一瞬间让我们相见",
            "闭上双眼 就不用担心 这月色也会慢慢沉浸"
        )

    music_tup2 = (   
            "我侧头痴痴注视着你茫然的眼睛 就如谎言一般绚丽像天青色一样澄净",
            "漫无目的跟随我在树荫里穿行 我信手拨弄身边花草随口道着它们的名",
            "对 垃圾当然要等垃圾桶满了才会去倒",
            "时雨敲过 几滩踏过 会不舍 廊柱斜落 微光洒落 痕斑驳",
            "沉郁结夏冰 冷而不清 轻叩幻梦 碎出无端秋萤",
            "说道揽望流风 有静美晴空 只怕一伫如梦 一瞬即永恒",
            "手中的熟悉药粒味道太苦 剥颗糖含才敢吞",
            "梦见在我脊椎生出双翼 却也只怀抱我成茧逃离",
            "黑夜终退潮明天终要来到 日落在下游谁又被垂钓",
            "答案仍未知晓 至少 能被你听到",
            "是成为大人模样 还是拥抱着微光",
            "安静闲暇的时间 平淡得可怕的从前",
            "逐渐慢下来的音乐 窗外正远去的世界 想把一切 封存在我的心海里面",
            "我们寻找着沿岸的浆果和深紫色花朵 然后让它们融合 成为了忧郁的颜色",
            "她曾说过像风样自由 飞过每个角落",
            "流星 它悄悄地落下 每一片结晶都在绚烂中升华",
            "念白 不重来 碎声 一点点 又继续"
    )

    music_tup3 = (
            "于是啜泣着妄想躲回夏天的怀抱",
            "怎么还没清醒 怎么还没清醒 未做完的梦 结成了厚冰",
            "走出 依旧喧闹的孤独",
            "沉郁结夏冰 冷而不清 轻叩幻梦 碎出无端秋萤",
            "借你一秒寂寥 换算一场舞蹈",
            "如此匆忙地度过 这段时间 然后去描绘生命吧",
            "将深埋回忆的滋味 全部融进这杯咖啡",
            "白日的灵魂 在夜晚破碎了",
            "窗外云忧郁着阴天 再无法自在地流连",
            "回首穆然发现曾经走过的路口 早已遍地秋叶落",
            "含苞待放的花 辉映着斑斓而凄美的晚霞",
            "塌陷在38°C的笑颜 没出现 不断经历着 渐渐麻木的痛觉",
            "抱歉没能梦到这星空 视线已逐渐变得朦胧"
)

    music_tup4 = (
            "它们是否也会轻阖哀伤湿漉漉地恳求时间暂停",
            "怎么还没清醒 怎么还没清醒 未做完的梦 结成了厚冰",
            "什么时候 开始变得 不向前走 与其不如是说 逐渐成为 讨厌的自我",
            "每天独自一人 打磨着那平凡生活 可是生活却没有善良对待我",
            "不断地 重复着 哀与恶",
            "消极声音钻进了噩梦",
            "遮挡住夜晚 也许就能 掩盖好作痛伤口",
            "闭上双眼 就不用担心 这月色也会慢慢沉浸",
)



    if ((output1 + output2 + output3)/3) >= 80 :
        dianping = dianping + "大吉"
        music_tup_num = random.randint(0,len(music_tup1)-1)
        music_dianping = music_dianping + music_tup1[music_tup_num]
        music_tup_num+= 100
    elif ((output1 + output2 + output3)/3) >=60 :
        dianping = dianping + "中吉"
        music_tup_num = random.randint(0,len(music_tup2)-1)
        music_dianping = music_dianping + music_tup2[music_tup_num]
        music_tup_num+= 200
    elif ((output1 + output2 + output3)/3) >=40 :
        dianping = dianping + "吉带凶，勉勉强强"
        music_tup_num = random.randint(0,len(music_tup3)-1)
        music_dianping = music_dianping + music_tup3[music_tup_num]
        music_tup_num+= 300
    else :
        dianping = dianping + "凶"
        music_tup_num = random.randint(0,len(music_tup4)-1)
        music_dianping = music_dianping + music_tup4[music_tup_num]
        music_tup_num+= 400

    if  output1 >= 80 :
        dianping = dianping + "，财源滚滚"
    if  output2 >= 80 :
        dianping = dianping + "，桃花灼灼"
    if  output3 >= 80 :
        dianping = dianping + "，春风得意"



    output1 = str(output1)
    output2 = str(output2)
    output3 = str(output3)
    # output4 = str(output4)

    ans = "诗岸为您祈愿今日份的美梦~\n您今日的运势为...\n今日财运:"+output1+"\n今日桃花运:"+output2+"\n今日事业运:"+output3+"\n点评:"+dianping+"\n \""+music_dianping+"\""

    await matcher.finish(ans)