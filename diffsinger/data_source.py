import asyncio
import time
import httpx

url="https://hf.space/embed/Silentlin/DiffSinger/+/api/predict/"
async def getWavBase64(jsonstr):
    async with httpx.AsyncClient() as client:
        data=jsonstr
        resp = await client.post(url,data=data,timeout=5000000)
        result = resp.json()
        return result
