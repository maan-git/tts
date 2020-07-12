import random

from app.utils.utils import create_dir, storage_file


class UserController:
    def __init__(self):
        pass

    def pic_user(self, **p):
        pass

    def _pic_user(self, **p):
        """
        :param: **p 
        """
        try:
            create_dir("/app/data")
            storage_file("/app/data", "users_file", users)
        except Exception as ex:
            raise Exception(ex)



@staticmethod
def user_controller():
    return UserController()