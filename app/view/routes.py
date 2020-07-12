from pyramid.response import Response
from pyramid.view import view_config

from app.controller.user_controller import user_controller


@view_config(route_name="helloworld", request_method="GET")
def hello_world(request):
    return Response("Hello World!")


@view_config(route_name="picuser", request_method="GET")
def pic_user(request):
    return Response("Testing")


@view_config(route_name="registerusers", request_method="POST")
def register_users(request):

    _user_controller = user_controller()
    _user_controller.pic_user()
    return Response(request)