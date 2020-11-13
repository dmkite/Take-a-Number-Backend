import cyclone.web
from twisted.internet import reactor

from src.api.ping_handler import PingHandler

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/ping", PingHandler),
        ]

        settings = dict(
            xheaders=False,
            static_path="./static",
            templates_path="./templates",
        )

        cyclone.web.Application.__init__(self, handlers, **settings)

def get_app():
    app = Application()
    reactor.listenTCP(8888, app)
    print("App started on port {}".format(8888))
    reactor.run()


if __name__ == "__main__":
    get_app()