from nonebot import on_command
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot import get_plugin_config
from .config import Config

from .data_source import get_f0, process_notes, bpm2dur
import asyncio
import json
import httpx

__plugin_meta__ = PluginMetadata(
    name="diffsinger",
    description="用DiffSinger让bot唱歌",
    usage="""
/diffsinger bpm~[[音高60,时值1,"pinyin"],[音高62,时值1,"pinyin"],...]
例：
/diffsinger 120~[
[60,2,"AP"],
[57,2,"ba"],
[59,2,"ni"],
[60,2,"peng"],
[64,2,"zai"],
[62,2,"shou"],
[60,2,"+"],
[62,8,"shang"],
[60,4,"AP"],
[57,2,"he"],
[59,2,"qi"],
[60,12,"le"],
[59,4,"shou"],
[55,16,"zhang"],
[60,4,"AP"]
]

""",
    type="application",
    config=Config,
    homepage="https://github.com/zhzhongshi/nonebot-plugin-diffsinger",
    supported_adapters={"~onebot.v11"}
)

ds = on_command("diffsinger", priority=7)
plugin_config = get_plugin_config(Config)
url = plugin_config.ds_url
ds_speedup = plugin_config.ds_speedup


async def send_request(method, url, data=None, params=None):
    async with httpx.AsyncClient() as client:
        if method == "GET":
            response = await client.get(url, params=params)
        elif method == "POST":
            response = await client.post(url, json=data)
        return response


@ds.handle()
async def sendcmd(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    arg = arg.extract_plain_text()
    preps = []
    lists = str(arg).split("|")
    for i in lists:
        notes = i.split("~")
        prep = bpm2dur(int(notes[0]), json.loads(notes[1]))
        preps.extend(prep)

    phone_dict = await send_request("GET", f"{url}getdict")
    req = process_notes(preps, phone_dict.json())
    phonemes = await get_rhythm(req)
    f0 = get_f0(req)
    model = "1215_opencpop_ds1000_fix_label_nomidi"
    submit_req = {
        "model": model,
        "phonemes": phonemes,
        "f0": {
            "timestep": 0.005,
            "values": f0
        },
        "speedup": ds_speedup
    }

    submit = await send_request("POST", f"{url}submit", submit_req)
    submit = submit.json()
    wav = None
    while True:
        await asyncio.sleep(1)
        stat = await send_request(
            "POST", f'{url}query',
            {"token": submit["token"]}
        )
        stat = stat.json()
        if stat["status"] == "HIT_CACHE":
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

    wav = await send_request(
        "GET", f"{url}download",
        params={"token": submit["token"]}
    )
    await ds.finish(MessageSegment.record(wav.content))


async def get_rhythm(req):
    resp = await send_request("POST", f"{url}rhythm", data=req)
    phonemes = resp.json()['phonemes']
    return phonemes
