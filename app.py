import json
import asyncio

import asyncpg
from aiohttp import ClientSession, web

from config import DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, TABLE
from config import WEB_HOST, WEB_PORT

app_storage = {}


async def save_to_db(pool, product):
    query = (
        f'INSERT INTO {TABLE}'
        '(id, title, description, price, discountpercentage, '
        'rating, stock, brand, category, thumbnail, images) '
        'VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)'
    )
    async with pool.acquire() as connection:
        await connection.execute(
            query,
            *tuple(product.values())[:-1],
            json.dumps(product['images'])
        )


async def get_products(number):
    url = 'https://dummyjson.com/products/'
    async with app_storage['session'].get(url=f'{url}/{number}') as response:
        product = await response.json()
        return product


async def handle(request):
    tasks = []
    pool = request.app['pool']
    try:
        count = int(request.rel_url.query['count'])
    except ValueError:
        result = 'Count of requests must be a number'
        return web.Response(text=result)

    if count <= 0:
        result = f'Count of requests must be more than 0 and ' \
                  f'less than 100. You entered: {count}'
    elif count > 100:
        result = f'Count of requests must be more than 0 and ' \
                 f'less than 100. You entered: {count}'
    else:
        for number in range(1, count + 1):
            tasks.append(asyncio.create_task(get_products(number)))

        for response in asyncio.as_completed(tasks):
            product = await response
            await save_to_db(pool, product)
        result = 'Done'

    return web.Response(text=result)


async def init():
    app_storage['session'] = ClientSession()

    async with app_storage['session']:
        app = web.Application()
        app['pool'] = await asyncpg.create_pool(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        app.add_routes([web.get('/', handle)])

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, WEB_HOST, WEB_PORT)
        await site.start()
        await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(init())
