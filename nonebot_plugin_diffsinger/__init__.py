from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.adapters.onebot.v11.event import  MessageEvent
from nonebot.params import CommandArg

from .data_source import get_f0, process_notes, bpm2dur

import json
import httpx
import time
ds = on_command("diffsinger", priority=7)
url="http://127.0.0.1:9266/"

    
@ds.handle()
async def sendcmd(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    preps=[]
    lists=str(arg).split("|")
    for i in lists:
        notes=i.split("~")
        prep=bpm2dur(int(notes[0]),json.loads(notes[1]))
        preps.extend(prep)
    
    phone_dict=httpx.request("GET",f"{url}getdict").json()
    req=process_notes(preps,phone_dict)
    phonemes=get_rhythm(req)
    f0=get_f0(req)
    model="1215_opencpop_ds1000_fix_label_nomidi"
    submit_req={
        "model": model,
        "phonemes":phonemes,
        "f0":{
            "timestep":0.005,
            "values":f0
        },
        "speedup": 50
    }
    
    submit=httpx.request("POST",f"{url}submit", json=submit_req).json()
    wav=None
    while True:
        time.sleep(1)
        stat=httpx.request("POST",f'{url}query', json={"token":submit["token"]}).json()
        if stat["status"]=="HIT_CACHE":
            break
        elif stat["status"] == "QUEUED":
            continue
        elif stat["status"] == "RUNNING":
            continue
        elif stat["status"] == "FINISHED":
            break
        elif stat["status"] == "FAILED":
            await ds.finish("错误："+stat["message"])
        elif stat["status"] == "CANCELLED":
            await ds.finish("已取消")
        
    wav=httpx.request("GET",f"{url}download",params={"token":submit["token"]}).content
    await ds.finish(MessageSegment.record(wav))
    
def get_rhythm(req):
    resp=httpx.request("POST",url+'rhythm', json=req)
    phonemes=resp.json()['phonemes']
    return phonemes
