import pytest
from photo_url.unsplash import get_photo


@pytest.mark.asyncio
async def test_get_photo():
    photo_url = await get_photo("Hfrcf")
    assert photo_url == None


@pytest.mark.asyncio
async def test_get_photo():
    photo_url = await get_photo("garage")
    assert photo_url == 'https://images.unsplash.com/photo-1486006920555-c77dcf18193c?crop=entropy&cs=tinysrgb&fit=' \
                        'max&fm=jpg&ixid=MnwyMjgzNTN8MHwxfHNlYXJjaHwxfHxnYXJhZ2V8ZW58MHx8fHwxNjIwNDgyMDAw&ixlib=rb-' \
                        '1.2.1&q=80&w=400'

