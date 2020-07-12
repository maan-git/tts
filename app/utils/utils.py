import os


def storage_file(*p):
    try:
        with open(f"{file_path}/{file_name}.txt", "w") as file:
            for dt in data_list:
                file.write(**dt)
                file.write("\n")
    except Exception as ex:
        raise Exception(f"Error trying to executing this operation: {ex}")


def check_file(*p):
    return os.path.isfile(f"{file_path}/{file_name}.txt")


def create_dir(*p):
    try:
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        return True
    except OSError as ex:
        raise OSError(f"Error trying to create the directory: {file_path}")
