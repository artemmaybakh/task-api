import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from main import tasks, app

@pytest_asyncio.fixture
async def client():
    tasks.clear()
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as c:
        yield c