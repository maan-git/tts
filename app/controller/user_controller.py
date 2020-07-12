import random

from app.utils.utils import create_dir, storage_file

from app.utils.config import BASE_DATA_PATH, FILE_NAME


class UserController:
    def __init__(self):
        self.data_dir = BASE_DATA_PATH
        self.file_name = FILE_NAME

    def pic_user(self, **p):
        pass

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
