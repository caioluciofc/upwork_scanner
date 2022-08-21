import uvloop
from sanic import Sanic
from sanic.response import json
from scanners.upwork_scanner import UpworkScanner
from helpers.exceptions import WrongUsernamePassword
import asyncio
import aiotask_context as context
from models.upwork_user import UpworkUser

app = Sanic("upwork-scanner")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/fetch_data')
async def fetch_user_data(request):
    upwork_scanner = UpworkScanner()
    request_args = request.args
    # http://127.0.0.1:5000/fetch_data?username=bobbybackupy&password=Argyleawesome123!

    if "username" not in request_args or "password" not in request_args:
        return json({"Error": "Required field missing"}, 400)

    username = request_args["username"][0]
    password = request_args["password"][0]

    try:
        data_fetched = await upwork_scanner.collect_user_data(username, password)
        user_model = UpworkUser(**data_fetched)
        user_model.write_to_db()
        return json(user_model.dict(), 200)
    except WrongUsernamePassword:
        return json({"Error": "Username or Password used is wrong"}, 400)


if __name__ == '__main__':
    asyncio.set_event_loop(uvloop.new_event_loop())
    serv_coro = app.create_server(
        host="127.0.0.1",
        port=5000,
        return_asyncio_server=True,
    )
    loop = asyncio.get_event_loop()
    # loop.set_task_factory(context.task_factory)
    serv_task = asyncio.ensure_future(serv_coro, loop=loop)
    server = loop.run_until_complete(serv_task)
    loop.run_until_complete(server.startup())
    loop.run_until_complete(server.before_start())
    loop.run_until_complete(server.after_start())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.run_until_complete(server.before_stop())

        # Wait for server to close
        close_task = server.close()
        loop.run_until_complete(close_task)

        # Complete all tasks on the loop
        for connection in server.connections:
            connection.close_if_idle()
        loop.run_until_complete(server.after_stop())