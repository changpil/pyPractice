class Logger(object):
    _instance = None
    def __init__(self):
        raise RuntimeError('Error: Call instance() instead')
    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance
    def __str__(self):
        return "singleton pattern"

try:
    l = Logger()
except RuntimeError as err:
    print(err)
    l = Logger.instance()

print(l)