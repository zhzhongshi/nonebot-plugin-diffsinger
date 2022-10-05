import base64
import asyncio
from re import T
import httpx
import json

from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.adapters.onebot.v11.event import  MessageEvent
from nonebot.typing import T_State
from nonebot.params import State, CommandArg
async def getWavBase64(jsonstr):
    url="https://hf.space/embed/Silentlin/DiffSinger/+/api/predict/"
    async with httpx.AsyncClient() as client:
        data=jsonstr
        resp = await client.post(url,data=data,timeout=5000)
        return resp
sing = on_command("歌声合成", priority=7)
@sing.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State = State(), arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    print(arg)
    resp=await getWavBase64(arg)
    result=resp.json()
    if resp.status_code != 200:
        dat=result['error']
        await sing.send("HTTP/1.1 "+str(resp.status_code)+"\n"+dat)
    else:
        dat=result['data'][0]
        headlessdat=str(dat).replace("data:audio/wav;base64,","")
        recmsg=MessageSegment.record(file=base64.b64decode(headlessdat))
        msg=Message(recmsg)
        await sing.send(msg)
    return 


# todo ["拍号",bpm,"歌词","谱子","时值"]
# t(tempo,拍号,时值)=(60/tempo)/16*时值

sang = on_command("合成歌声", priority=7)
@sang.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State = State(), arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    print(arg)
    # 参数处理
    seq=json.loads(arg)
    # 参数解析,计算时值
    arg1=str(seq[0]).split("/")
    phfm=arg1[1]
    bpm=seq[1]
    lyric=str(seq[2])
    note_per_word_lst = [x.strip() for x in str(seq[3]).split('|') if x.strip() != '']
    mididur_per_word_lst = [x.strip() for x in str(seq[4]).split('|') if x.strip() != ''] # [1,1,2 2,2]
    if not len(note_per_word_lst) == len(mididur_per_word_lst):
        await sang.send("请检查歌词|音符|时值数量是否一致")
    else: 
        # 构造json
        dur_per_word_lst=[]
        for i in mididur_per_word_lst:
            mididur_per_note=i.split(" ")
            if len(mididur_per_note) >1:
                midpnote=[] # [2 2]
                for m in mididur_per_note:
                    j=float(m)
                    t = float ((60/int(bpm)/int(phfm)) * j)
                    t2=round(t,7)
                    midpnote.append(str(t2))
                midpword=str(" ".join(midpnote))
                dur_per_word_lst.append(midpword)
            else:
                j=float(i)
                t = float ((60/int(bpm)/int(phfm)) * j)
                t2=round(t,7)
                dur_per_word_lst.append(str(t2))
        stringque=str("|".join(dur_per_word_lst))
        notes=str("|".join(note_per_word_lst))
        datas=[lyric,notes,stringque]
        data={"data":datas}
        jsonobj=json.dumps(data)
        print(jsonobj)
        await sang.send("开始合成")
        resp=await getWavBase64(jsonobj)
        result=resp.json()
        if resp.status_code != 200:
            dat=json.dumps(result)
            await sang.send("HTTP/1.1 "+str(resp.status_code)+"\n"+dat)
        else:
            dat=result['data'][0]
            headlessdat=str(dat).replace("data:audio/wav;base64,","")
            recmsg=MessageSegment.record(file=base64.b64decode(headlessdat))
            msg=Message(recmsg)
            await sang.send(msg)
    return 
