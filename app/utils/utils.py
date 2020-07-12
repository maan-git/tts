import os


def storage_file(**p):
    try:
        with open(f"{p['file_path']}/{p['file_name']}.txt", "w") as file:
            for x, dt in enumerate(p["data_list"]):
                file.write(dt)
                if x+1 != len(dt):
                    file.write("\n")
    except Exception as ex:
        raise Exception(f"Error trying to executing this operation: {ex}")


def _check_file(*p):
    return os.path.isfile(f"{p[0]}/{p[1]}.txt")


def create_dir(*p):
    try:
        if not os.path.isdir(p[0]):
            os.mkdir(p[0])
        return True
    except OSError as ex:
        raise OSError(f"Error trying to create the directory: {p[0]}")


def read_file(*p):
    try:
        if _check_file(p[0], p[1]):
            res = []
            with open(f"{p[0]}/{p[1]}.txt", "r") as file:
                _res = file.read()
                _res = _res.split("\n")
                res = list(filter(None, _res))
            return res
        else:
            raise Exception("There is no users file")
    except Exception as ex:
        raise Exception(f"Error trying to get the users from file {p[1]}: {ex}")


def delete_register_in_file(*p):
    try:
        res = read_file(*p)
        storage_file(file_path=p[0], file_name=p[1], data_list=res)
        return True
    except Exception as ex:
        raise Exception(
            f"Error trying to remove {p[2]} the users from file {p[1]}: {ex}"
        )