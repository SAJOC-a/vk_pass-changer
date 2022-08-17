def file_open(path, mode):
    try:
        file = open(path, mode)
        return file
    except:
        pass
    try:
        file = open(path, mode, encoding='utf-8')
        return file
    except:
        pass
    try:
        file = open(path, mode, encoding='iso-8859-1')
        return file
    except:
        pass