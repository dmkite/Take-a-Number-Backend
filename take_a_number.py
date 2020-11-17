import cyclone.web
from twisted.internet import defer, reactor

from src.api.ping_handler import PingHandler
from src.api.queue_handler import QueueHandler
import src.lib.redis as redis

class Application(cyclone.web.Application):
    def __init__(self, redis_conn):
        self.redis_conn = redis_conn
        handlers = [
            (r"/ping", PingHandler),
            (r"/queue", QueueHandler)
        ]

        settings = dict(
            xheaders=False,
            static_path="./static",
            templates_path="./templates",
        )

        cyclone.web.Application.__init__(self, handlers, **settings)

def get_app():
    redis_conn = redis.Connection()
    app = Application(redis_conn)
    reactor.listenTCP(8888, app)
    print("App started on port {}".format(8888))
    reactor.run()


if __name__ == "__main__":
    get_app()