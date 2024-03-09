import asyncio
import requests
import multiprocessing
from timer import timer 
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

url = "https://httpbin.org/uuid"


async def fetch_uuid(session,url):
   async with session.get(url) as response:
        json_data = await response.json()
        print(json_data['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        task = [fetch_uuid(session,url) for _ in range(100)]
        await asyncio.gather(*task)




async def main():
    

