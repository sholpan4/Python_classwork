class Logger:
    Instance = None
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.Instance = super(Logger, cls).__new__(cls)
        return cls.Instance

    def __init__(self, log_level, stdout = True, file=None):
        self.log_level = log_level
        self.stdout = stdout
        self.file = file
        Logger.Instance = self

    