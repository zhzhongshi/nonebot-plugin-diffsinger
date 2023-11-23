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
@sing.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    print(arg)
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

