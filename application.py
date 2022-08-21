import uvloop
from sanic import Sanic
from sanic.response import json
from mainzao import UpworkScanner
import asyncio
import aiotask_context as context
import pymongo
from models.upwork_user import UpworkUser


app = Sanic("my-hello-world-app")

client = pymongo.MongoClient(
    "mongodb+srv://earthdni:oIB0OdI69touYewU@cluster0.b2o9p.mongodb.net/?retryWrites=true&w=majority")
db = client.test


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/fetch_data')
async def fetch_user_data(request):
    upwork_scanner = UpworkScanner()
    data_fetched = await upwork_scanner.collect_user_data()
    user_model = UpworkUser(**data_fetched)
    print(user_model)
    print(user_model.user_rid)
    print(data_fetched)
    return json(data_fetched)

if __name__ == '__main__':
    asyncio.set_event_loop(uvloop.new_event_loop())
    serv_coro = app.create_server(
        host="127.0.0.1",
        port=5000,
        return_asyncio_server=True,
    )
    loop = asyncio.get_event_loop()
    loop.set_task_factory(context.task_factory)
    serv_task = asyncio.ensure_future(serv_coro, loop=loop)
    server = loop.run_until_complete(serv_task)
    server.after_start()
    loop.run_forever()