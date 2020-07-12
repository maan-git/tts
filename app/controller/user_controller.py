import random

from app.utils.utils import create_dir, storage_file, read_file
from app.utils.config import BASE_DATA_PATH, FILE_NAME


class UserController:
    def __init__(self):
        self.data_dir = BASE_DATA_PATH
        self.file_name = FILE_NAME

    def pic_user(self):
        try:
            return self._pic_user()
        except Exception as ex:
            raise Exception(f"Error trying to select an user: {ex}")

    def _pic_user(self):
        try:
            res = read_file(self.data_dir, self.file_name)
            user_res = "No more users =/"
            if len(res) > 0:
                print(f"Users: {res}")
                _user_res = random.randrange(0, len(res), 1)
                user_res = res[_user_res]
                res_new = list(filter(lambda x: x != res[_user_res], res))
                storage_file(
                    file_path=self.data_dir, file_name=self.file_name, data_list=res_new
                )
            return user_res
        except Exception as ex:
            raise Exception(ex)

    def register_users(self, *args):

        try:
            self._register_users(*args)
        except Exception as ex:
            raise Exception(f"Error trying to register the users: {ex}")

    def _register_users(self, *p):
        """
        :param: *p 
        """
        try:
            create_dir(self.data_dir)
            storage_file(
                file_path=self.data_dir, file_name=self.file_name, data_list=p[0]
            )
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def user_controller():
        return UserController()
