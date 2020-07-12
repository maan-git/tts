from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from app.utils.config import BASE_API_PATH


def run_app():
    with Configurator() as config:
        config.add_route("hello", f"{BASE_API_PATH}/")
        config.add_view(routes.hello_world, route_name="hello")

        config.add_route("picuser", f"{BASE_API_PATH}/picuser")
        config.add_view(routes.pic_user, route_name="picuser")

        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()


if __name__ == "__main__":
    try:
        from app.view import routes
        print("Running up the API")
        run_app()
    except Exception as ex:
        raise Exception(f"Error trying to import the routes: {ex}")
