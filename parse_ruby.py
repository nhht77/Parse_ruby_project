from os import path

def getTargetPath(p):
    data = path.realpath(p)
    target = ("/" + data.replace("\\", "/"))
    return target

target = getTargetPath("config.ru")
print(target)

