from twisted.python import log
from enum import Enum

class LogLevel(Enum):
    TRACE = 1
    DEBUG = 10
    INFO = 100
    WARN = 1000
    ERROR = 10000

class Logger():
    is_prod = False
    log_level = LogLevel.TRACE
    def log(self, msg, log_level=LogLevel.TRACE, **kwargs):
        if log_level.value >= self.log_level.value:
            log.msg(msg)
        print(
            'lvl={}'.format(self.log_level), 
            'msg={}'.format(msg), 
            **kwargs)
