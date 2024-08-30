from pathlib import Path

import nonebot
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,GroupRequestEvent


from .config import Config

import sqlite3


__plugin_meta__ = PluginMetadata(
    name="test",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

sub_plugins = nonebot.load_plugins(
    str(Path(__file__).parent.joinpath("plugins").resolve())
)





test = on_command("test_t")
select = on_command("test_select")
type = on_command("test_type")
delete_all = on_command("test_delete_all")
sall = on_command("test_all")



@test.handle()
async def _(event: GroupMessageEvent):
    db = sqlite3.connect('demo.db')
    cursor = db.cursor()
    await test.send("ping!")
    data = [(event.user_id,100)]
    sql = 'insert OR IGNORE into affection_table values (?, ?)'
    cursor.executemany(sql, data)
    db.commit()
    cursor.close()
    db.close()

    await test.finish("pong")



@select.handle()
async def _(event: GroupMessageEvent):
    db = sqlite3.connect('demo.db')
    cursor = db.cursor()
    sql = 'select affection_level from affection_table where id =  (?) ' #寻找好感度
    cursor.execute(sql,(event.user_id,))
    result = cursor.fetchall()
    
    if len(result) == 0 :

        data = [(event.user_id,100)]
        sql = 'insert OR IGNORE into affection_table values (?, ?)'
        cursor.executemany(sql, data)
        db.commit()
        result_ans = "检查到您还没有开启好感度系统，您现在的好感度是100"
    else:
        result_ans = str(result)
        result_ans = "您现在的好感度是" + result_ans[2:-3]
    await select.send(result_ans)
    cursor.close()
    db.close()

    await select.finish("pong")

@type.handle()
async def _(event: GroupMessageEvent):
    id = event.user_id
    id = str(id)
    await select.send(id)
    await select.finish("pong")


@delete_all.handle()
async def _(event: GroupMessageEvent):
    # DELETE FROM COMPANY WHERE ID = 7
    db = sqlite3.connect('demo.db')
    cursor = db.cursor()
    sql = 'DELETE FROM affection_table'
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    await select.finish("pong")

@sall.handle()
async def _(event: GroupMessageEvent):
    db = sqlite3.connect('demo.db')
    cursor = db.cursor()
    sql = 'select * from affection_table ' 
    cursor.execute(sql)
    result = cursor.fetchall()
    result = str(result)
    await select.send(result)
    await select.finish("pong")












    #id                  int  primary key   not null,
    #affection_level     int