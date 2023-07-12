import base64
import httpx
import json
import time

from urllib.request import urlopen
from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.adapters.onebot.v11.event import  MessageEvent
from nonebot.params import CommandArg

async def submit(data):
    url="http://43.140.195.208:9266/submit"
    async with httpx.AsyncClient() as client:
        resp = await client.post(url,data=data,headers={"Content-Type":"application/json"})
        return resp

async def query(token):
    url="http://43.140.195.208:9266/query"
    async with httpx.AsyncClient() as client:
        resp = await client.post(url,data=token)
        return resp
    
data='''
{"model": "1215_opencpop_ds1000_fix_label_nomidi", "phonemes": [{"name": "AP", "duration": 0.156001}, {"name": "j", "duration": 0.119999}, {"name": "ian", "duration": 0.127002}, {"name": "d", "duration": 0.044998}, {"name": "e", "duration": 0.128002}, {"name": "w", "duration": 0.044998}, {"name": "ei", "duration": 0.111999}, {"name": "f", "duration": 0.060001}, {"name": "eng", "duration": 0.087852}, {"name": "ch", "duration": 0.085148}, {"name": "ui", "duration": 0.284002}, {"name": "g", "duration": 0.059998}, {"name": "uo", "duration": 0.255}, {"name": "h", "duration": 0.09}, {"name": "uan", "duration": 0.112999}, {"name": "h", "duration": 0.060001}, {"name": "uan", 
"duration": 0.094546}, {"name": "f", "duration": 0.077454}, {"name": "u", "duration": 0.285002}, {"name": "g", "duration": 0.059998}, {"name": "uo", "duration": 0.112002}, {"name": "l", "duration": 0.059998}, {"name": "e", "duration": 0.319999}, {"name": "er", "duration": 0.138328}, {"name": "p", "duration": 0.059673}, {"name": "an", "duration": 0.948}, {"name": "AP", "duration": 0.213002}, {"name": "n", "duration": 0.044998}, {"name": "i", "duration": 0.128002}, {"name": "d", "duration": 0.044998}, {"name": "e", "duration": 0.126998}, {"name": "r", "duration": 0.045002}, {"name": "ong", "duration": 0.147998}, {"name": "y", "duration": 0.025002}, {"name": "En", "duration": 0.689}, {"name": "SP", "duration": 0.069}], "f0": {"timestep": 0.005, "values": [317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 317.1, 296.8, 296.7, 296.5, 296.2, 295.9, 295.6, 295.2, 294.7, 
294.3, 293.9, 293.6, 293.3, 293.2, 293.2, 292.8, 292.5, 293.0, 293.8, 294.1, 295.3, 296.5, 297.6, 298.0, 297.9, 297.4, 296.6, 295.7, 294.4, 292.6, 291.3, 289.5, 288.0, 288.0, 288.5, 289.6, 295.4, 304.9, 308.9, 310.8, 311.8, 311.8, 311.9, 312.4, 312.7, 313.0, 313.5, 313.7, 313.6, 313.1, 312.4, 311.3, 310.4, 309.8, 309.0, 308.3, 307.7, 306.8, 305.4, 303.9, 302.6, 301.2, 299.4, 297.9, 297.8, 297.8, 297.5, 297.3, 297.1, 296.8, 296.5, 296.0, 295.7, 295.3, 295.0, 294.7, 294.4, 294.2, 294.0, 294.0, 294.0, 294.0, 294.0, 294.1, 294.2, 294.2, 294.3, 294.3, 294.5, 293.2, 290.3, 286.0, 280.6, 274.7, 269.9, 266.0, 264.0, 263.3, 263.1, 263.1, 263.0, 262.9, 262.7, 262.6, 262.4, 262.2, 262.1, 261.9, 261.9, 261.9, 261.9, 261.8, 261.6, 261.5, 261.2, 261.0, 260.7, 260.5, 260.4, 260.3, 260.1, 259.2, 257.7, 255.3, 252.4, 248.9, 245.4, 242.2, 239.2, 236.6, 235.0, 234.3, 234.2, 234.3, 234.5, 234.8, 235.2, 235.7, 236.2, 236.7, 237.2, 237.6, 237.9, 238.1, 238.2, 238.0, 237.6, 237.0, 236.2, 235.4, 234.6, 234.0, 233.8, 233.7, 233.0, 232.5, 232.3, 232.3, 232.4, 232.9, 233.1, 233.5, 233.8, 233.9, 233.9, 234.0, 234.1, 234.0, 233.8, 233.6, 233.5, 233.4, 233.3, 233.1, 232.9, 232.7, 232.9, 233.0, 
233.4, 233.6, 233.9, 234.1, 234.3, 234.4, 234.5, 234.6, 234.4, 233.7, 232.7, 231.5, 230.8, 231.7, 234.4, 238.5, 240.0, 241.5, 243.0, 244.5, 246.0, 247.5, 249.0, 250.6, 252.1, 253.7, 255.3, 256.8, 258.4, 260.0, 261.6, 263.2, 264.9, 266.5, 253.9, 247.6, 244.2, 242.3, 240.6, 238.8, 237.2, 236.1, 235.0, 233.9, 233.3, 233.0, 232.7, 232.3, 232.4, 232.4, 232.5, 232.7, 232.9, 232.9, 232.9, 232.9, 233.1, 233.2, 233.2, 233.0, 232.9, 232.5, 232.4, 232.4, 232.4, 232.6, 232.8, 233.0, 233.4, 233.9, 234.3, 234.6, 234.8, 234.5, 234.0, 233.1, 231.9, 230.4, 228.3, 226.3, 224.8, 222.8, 219.7, 218.4, 219.4, 221.7, 224.0, 226.3, 228.6, 230.9, 233.3, 235.7, 238.1, 240.6, 243.0, 245.5, 248.0, 250.6, 253.1, 255.7, 258.4, 261.0, 253.9, 246.2, 243.9, 242.2, 240.1, 238.7, 237.9, 236.7, 235.2, 234.3, 233.7, 233.3, 232.5, 232.0, 231.4, 230.8, 230.1, 229.5, 228.8, 228.1, 227.5, 227.0, 226.9, 227.2, 226.4, 226.1, 217.4, 234.8, 235.1, 235.7, 236.5, 237.3, 238.0, 238.8, 241.3, 247.9, 256.2, 261.3, 263.2, 263.1, 263.1, 263.0, 263.0, 262.9, 262.8, 262.6, 262.5, 262.4, 262.4, 262.4, 261.9, 260.5, 258.1, 254.6, 250.0, 245.8, 242.0, 238.7, 236.2, 234.8, 247.2, 247.6, 247.9, 248.2, 248.6, 248.9, 249.2, 
249.6, 249.9, 250.3, 249.9, 246.7, 244.0, 241.9, 240.5, 238.5, 237.5, 236.0, 234.8, 234.1, 233.6, 232.8, 232.2, 231.9, 231.7, 231.6, 231.6, 231.6, 231.7, 231.9, 232.1, 232.5, 232.7, 232.9, 233.0, 233.2, 233.1, 232.8, 232.7, 232.7, 232.7, 232.9, 233.0, 233.2, 233.4, 233.6, 233.9, 234.1, 234.0, 233.7, 233.4, 232.5, 231.6, 230.9, 230.3, 229.7, 228.4, 226.7, 224.8, 222.8, 221.8, 221.8, 223.0, 226.0, 229.5, 233.0, 236.6, 240.3, 244.0, 247.8, 251.6, 262.8, 262.8, 262.9, 263.0, 263.1, 263.1, 263.2, 263.4, 263.5, 263.6, 263.7, 263.8, 263.9, 263.9, 264.0, 263.8, 263.5, 262.8, 262.0, 261.0, 259.8, 258.6, 257.6, 256.7, 256.0, 255.6, 255.4, 254.5, 253.3, 251.8, 250.2, 249.5, 249.6, 249.0, 248.1, 245.8, 242.7, 240.1, 238.3, 237.5, 237.4, 237.4, 237.3, 237.1, 237.0, 236.8, 236.6, 236.3, 236.1, 235.8, 235.6, 235.4, 235.1, 234.9, 234.8, 234.7, 234.6, 234.6, 234.5, 234.4, 234.1, 233.9, 233.6, 233.2, 232.8, 232.4, 232.2, 232.0, 231.9, 231.9, 231.9, 232.0, 232.1, 232.4, 232.5, 232.7, 232.9, 232.9, 233.0, 232.8, 232.1, 230.7, 228.8, 226.8, 224.4, 221.9, 219.0, 216.5, 214.4, 212.5, 210.9, 209.6, 209.0, 209.0, 209.0, 209.3, 209.8, 210.3, 210.8, 211.3, 211.8, 212.1, 212.3, 212.2, 212.0, 
211.7, 211.3, 210.9, 210.4, 209.9, 209.5, 209.1, 208.7, 208.4, 208.3, 208.3, 208.1, 207.5, 206.7, 205.7, 204.5, 203.1, 201.7, 199.9, 198.4, 197.1, 195.8, 194.6, 193.7, 193.2, 192.9, 193.0, 197.0, 198.0, 199.0, 200.0, 201.0, 202.0, 203.0, 204.0, 205.0, 206.1, 207.1, 208.1, 209.2, 210.2, 210.8, 209.7, 208.4, 206.2, 203.6, 201.6, 199.8, 198.8, 198.2, 197.2, 196.7, 196.3, 195.9, 195.8, 195.6, 195.6, 195.7, 195.8, 195.9, 195.9, 195.5, 195.3, 195.1, 194.6, 194.6, 194.6, 194.4, 194.4, 194.4, 194.5, 194.6, 194.9, 195.3, 195.5, 195.8, 196.1, 196.3, 196.6, 196.8, 197.1, 197.2, 197.2, 197.4, 197.4, 197.4, 197.4, 197.4, 197.4, 197.3, 197.1, 197.0, 196.9, 196.7, 196.7, 196.5, 196.2, 196.0, 195.5, 195.3, 195.2, 194.9, 194.8, 194.8, 194.9, 195.5, 195.6, 195.9, 196.1, 196.4, 196.7, 197.1, 197.5, 198.1, 198.3, 198.5, 198.7, 198.7, 198.8, 198.8, 198.7, 198.7, 198.5, 198.3, 198.0, 197.2, 197.0, 196.5, 196.1, 195.7, 195.4, 194.8, 194.3, 193.8, 193.2, 192.9, 192.8, 192.9, 193.2, 193.4, 193.7, 194.1, 194.5, 195.5, 196.1, 196.7, 197.6, 198.2, 198.7, 199.3, 199.8, 200.3, 200.6, 200.6, 200.5, 200.2, 200.0, 199.7, 199.2, 198.9, 198.5, 198.0, 197.5, 196.9, 196.1, 195.4, 194.9, 194.5, 194.2, 
193.8, 193.4, 193.1, 192.9, 192.7, 192.8, 193.1, 193.5, 194.2, 194.7, 195.3, 196.0, 196.5, 197.1, 197.7, 198.4, 198.9, 199.5, 200.0, 200.4, 200.5, 200.6, 200.5, 200.2, 200.0, 199.8, 199.5, 199.1, 198.6, 198.0, 197.5, 197.0, 196.5, 196.1, 195.9, 195.7, 195.4, 195.3, 194.9, 194.7, 194.5, 194.6, 194.8, 195.6, 197.0, 197.8, 198.2, 198.7, 199.3, 199.6, 199.8, 199.4, 199.0, 197.7, 196.5, 194.6, 192.5, 191.0, 190.2, 189.7, 189.5, 189.4, 189.7, 191.3, 192.8, 194.4, 196.0, 197.6, 199.2, 200.8, 202.4, 204.1, 205.7, 207.4, 209.1, 210.8, 212.5, 214.2, 216.0, 217.7, 219.5, 221.3, 223.1, 224.9, 226.7, 228.6, 230.4, 232.3, 234.2, 236.1, 238.0, 240.0, 241.9, 243.9, 245.9, 247.9, 249.9, 251.9, 230.3, 230.3, 230.3, 230.3, 230.3, 230.3, 230.2, 230.1, 230.1, 230.1, 230.0, 230.0, 230.0, 230.0, 230.0, 230.0, 230.0, 230.2, 230.6, 231.0, 231.5, 232.1, 232.5, 232.8, 232.9, 233.1, 233.1, 233.1, 233.1, 233.2, 233.2, 233.2, 233.3, 233.1, 232.2, 230.4, 227.9, 224.5, 221.6, 219.2, 217.5, 216.6, 214.5, 215.1, 221.2, 227.5, 234.0, 240.7, 247.5, 254.5, 261.8, 260.6, 261.3, 261.2, 261.4, 261.6, 261.3, 260.5, 259.4, 258.3, 257.2, 256.4, 255.5, 254.3, 253.7, 253.7, 255.1, 256.9, 259.8, 262.2, 264.3, 
265.7, 269.4, 273.3, 276.9, 280.1, 282.4, 284.2, 285.6, 287.1, 287.9, 288.5, 288.7, 289.1, 289.3, 290.0, 290.4, 291.1, 291.7, 292.3, 293.0, 293.6, 294.0, 294.4, 294.7, 295.0, 295.1, 295.4, 295.4, 295.7, 295.6, 295.0, 294.5, 293.7, 293.2, 293.1, 293.5, 294.4, 295.8, 297.2, 298.9, 300.3, 301.9, 304.0, 305.4, 306.8, 308.8, 310.1, 311.1, 312.2, 313.3, 314.1, 314.8, 315.6, 315.9, 316.0, 316.0, 315.7, 315.4, 314.9, 314.4, 313.8, 313.1, 312.5, 312.1, 311.6, 311.2, 310.9, 310.3, 309.7, 309.2, 308.7, 308.4, 308.3, 308.5, 308.6, 308.9, 309.2, 309.6, 310.1, 310.3, 310.8, 311.1, 311.5, 311.8, 312.2, 312.5, 312.6, 312.6, 312.8, 313.1, 313.3, 313.5, 313.5, 313.1, 312.8, 312.6, 312.4, 311.8, 311.2, 310.7, 310.3, 310.3, 310.4, 310.4, 310.2, 310.2, 310.1, 310.2, 310.4, 310.4, 310.4, 310.4, 310.4, 310.4, 310.4, 310.5, 310.7, 310.9, 311.2, 311.3, 311.3, 311.1, 310.8, 310.3, 310.1, 309.6, 309.3, 309.0, 308.9, 308.8, 308.8, 308.8, 308.9, 309.1, 309.5, 309.8, 310.0, 310.4, 310.9, 311.5, 311.9, 312.4, 312.7, 312.9, 312.8, 312.9, 312.8, 312.7, 312.7, 312.6, 312.4, 312.5, 312.4, 312.5, 312.4, 312.4, 312.4, 312.2, 311.9, 311.6, 311.1, 310.6, 310.1, 309.7, 309.3, 309.2, 309.2, 309.4, 310.1, 
311.3, 312.0, 313.4, 314.0, 314.3, 314.1, 312.9, 311.4, 309.4, 307.3, 305.3, 304.2, 304.0, 303.9, 302.2, 300.1, 297.2, 290.9, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8, 287.8]}, "speedup": 50}
'''
sing = on_command("测试", priority=7)
@sing.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
    arg = arg.extract_plain_text()
    # todo 传入参数
    
    
    json_data=json.loads(data)
    resp=await submit(json.dumps(json_data))
    result=resp.json()
    token=result["token"]
    status=result["status"]
    while status != "HIT_CACHE":
        time.sleep(3)
        status_query=await query(token=json.dumps({"token":token}))
        query_res=status_query.json()
        # todo 状态判断 队列
        status=query_res["status"]
        if status == ("FAILED" or "CANCELLED"):
            sing.send("出错")
            break
    if status=="HIT_CACHE":
        recmsg=MessageSegment.record(file="http://43.140.195.208:9266/download?token="+token)
        await sing.finish(Message(recmsg))

        

'''
# todo ["拍号",bpm,"歌词","谱子","时值"]
# t(tempo,拍号,时值)=(60/tempo)/16*时值

sang = on_command("合成歌声", priority=7)
@sang.handle()
async def _(bot: Bot, event: MessageEvent, arg: Message=CommandArg()):
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
        durs=str("|".join(dur_per_word_lst))
        notes=str("|".join(note_per_word_lst))
        datas=[lyric,notes,durs]
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
'''
