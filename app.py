import json
import asyncio
import asyncpg
from aiohttp import ClientSession, web

app_storage = {}


async def save_to_db(pool, product):
    query = (
        'INSERT INTO products' 
        '(id, title, description, price, discountpercentage, '
        'rating, stock, brand, category, thumbnail, images) '
        'VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)'
    )
    async with pool.acquire() as connection:
        async with connection.transaction():
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
        return web.Response(text=json.dumps(result))

    if count <= 0:
        result = 'Count of requests must be more than 0 and ' \
                 'less than 100. You entered: {}'.format(count)
    elif count > 100:
        result = 'Count of requests must be more than 0 and ' \
                 'less than 100. You entered: {}'.format(count)
    else:
        for number in range(1, count + 1):
            tasks.append(asyncio.create_task(get_products(number)))

        for response in asyncio.as_completed(tasks):
            product = await response
            await save_to_db(pool, product)
        result = 'Done'

    return web.Response(text=json.dumps(result))


async def init():
    app_storage['session'] = ClientSession()

    async with app_storage['session']:
        app = web.Application()
        app['pool'] = await asyncpg.create_pool(
            database='postgres',
            user='postgres',
            password='postgres',
            host='postgres',
            port=3306
        )
        app.add_routes([web.get('/', handle)])

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8080)
        await site.start()
        await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(init())
