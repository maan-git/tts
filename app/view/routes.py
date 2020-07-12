from pyramid.response import Response
from app.controller.user_controller import UserController


def hello_world(request):
    return {"message": "Hello World!"}


def pic_user(request):
    _user_controller = UserController.user_controller()
    res = _user_controller.pic_user()

    return {"data": res}


def register_users(request):
    users = request.json_body.get("users", "user was not provided")

    _user_controller = UserController.user_controller()
    _user_controller.register_users(users)

    return {"data": request.json_body.get("users", "user was not provided")}
