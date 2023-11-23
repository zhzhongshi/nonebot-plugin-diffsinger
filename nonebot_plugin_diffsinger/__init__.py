import base64
import asyncio
import httpx
import json
import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.adapters.onebot.v11.event import  MessageEvent
from nonebot.params import CommandArg
async def getWavId(jsonstr):
    url="http://127.0.0.1:8000/api/infer/"
    async with httpx.AsyncClient() as client:
        data=jsonstr
        resp = await client.post(url,data=data,timeout=280)
        return resp
def getWav(id):
    url="http://127.0.0.1:8000/api/getwav/"
    resp = requests.get(url=(url+"?uuid="+id))
    return resp.content
sing = on_command("ds", priority=7)
sang = on_command("dstest", priority=8)
@sing.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    print(arg)
    await sing.send("开始合成")
    resp=await getWavId(arg)
    result=resp.json()
    if resp.status_code != 200:
        dat=result['error']
        await sing.send("HTTP/1.1 "+str(resp.status_code)+"\n"+dat)
    else:
        id=result['id']
        recmsg=MessageSegment.record(file=bytes(getWav(id)))
        msg=Message(recmsg)
        await sing.send(msg)
    return 

@sang.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    print(arg)
    arg=note2data(arg)
    await sing.send("开始合成")
    resp=await getWavId(arg)
    result=resp.json()
    if resp.status_code != 200:
        dat=result['error']
        await sing.send("HTTP/1.1 "+str(resp.status_code)+"\n"+dat)
    else:
        id=result['id']
        recmsg=MessageSegment.record(file=bytes(getWav(id)))
        msg=Message(recmsg)
        await sing.send(msg)
    return 
'''
{"tempo":120,"data":
["小酒窝长睫毛AP是你最美的记号",
"C#4 | F#4| G#4 | A#4 F#4 | F#4 C#4 | C#4 | rest | C#4 | A#4 | G#4 | A#4 | G#4 | F4 | C#4",
"2 |2 | 2 | 2 2 | 2 2 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2"]
}
'''
def note2data(arg: str):
    print(arg)
    # 参数处理
    seq=json.loads(arg)
    
    # 参数解析,计算时值
    bpm=seq["tempo"]
    lrcdata=seq["data"]
    lyric=str(lrcdata[0])
    note_per_word_lst = [x.strip() for x in str(lrcdata[1]).split('|') if x.strip() != '']
    mididur_per_word_lst = [x.strip() for x in str(lrcdata[2]).split('|') if x.strip() != ''] # [1,1,2 2,2]
    if not len(note_per_word_lst) == len(mididur_per_word_lst):
        return "{\"error\":\"长度不一致\"}"
    else: 
        # 构造json
        dur_per_word_lst=[]
        for i in mididur_per_word_lst:
            mididur_per_note=i.split(" ")
            if len(mididur_per_note) >1:
                midpnote=[] # [2 2]
                for m in mididur_per_note:
                    if not(m==""):
                        # 16分音符
                        j=float(m)
                        # 该音符时长
                        t = float ((60/int(bpm)/4)*j)
                        # 保留7位小数
                        t2=round(t,7)
                        midpnote.append(str(t2))
                midpword=str(" ".join(midpnote))
                dur_per_word_lst.append(midpword)
            else:
                # 16分音符
                j=float(i)
                # 该音符时长
                t = float ((60/int(bpm)/4)*j)
                # 保留7位小数
                t2=round(t,7)
                dur_per_word_lst.append(str(t2))
        durs=str("|".join(dur_per_word_lst))
        notes=str("|".join(note_per_word_lst))
        datas=[lyric,notes,durs]
        data={"data":datas}
        jsonobj=json.dumps(data)
        print(jsonobj)
        return jsonobj
