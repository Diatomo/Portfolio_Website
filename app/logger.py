

import datetime
from app import app


class Logger:

    def __init__(self):
        pass


    def timestampLog(self):
        dt = datetime.datetime.now()
        result = str(dt) + ': '
        return result

    def addEntry(self, level, msg):
        if (level == 'info'):
            app.logger.info(self.timestampLog() + msg)
