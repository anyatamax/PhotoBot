import aiohttp
import json
import os


async def get_photo(text):
    url = 'https://api.unsplash.com/search/photos?client_id={}&query={}&page=1&per_page=2&lang=en'\
        .format(os.environ['token_unsplash'], text)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            answer = await resp.read()
            response = json.loads(answer)
            if not response['results']:
                return None
            url_photo = response['results'][0]['urls']['small']
            return url_photo
