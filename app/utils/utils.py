import os


def storage_file(**p):

    try:
        with open(f"{p['file_path']}/{p['file_name']}.txt", "w") as file:
            for dt in p["data_list"]:
                file.write(dt)
                file.write("\n")
    except Exception as ex:
        raise Exception(f"Error trying to executing this operation: {ex}")


def check_file(*p):
    return os.path.isfile(f"{p[0]}/{p[1]}.txt")


def create_dir(*p):
    try:
        if not os.path.isdir(p[0]):
            os.mkdir(p[0])
        return True
    except OSError as ex:
        raise OSError(f"Error trying to create the directory: {p[0]}")
