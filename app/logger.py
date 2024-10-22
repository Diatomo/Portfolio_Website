

from datetime import datetime
from app import app
from zoneinfo import ZoneInfo

class Logger:

    def __init__(self):
        pass


    def timestampLog(self):
        utc_time = datetime.now(ZoneInfo("UTC"))
        est_time = utc_time.astimezone(ZoneInfo("America/New_York"))
        result = str(est_time) + ': '
        return result

    def addEntry(self, level, msg):
        if (level == 'info'):
            app.logger.info(self.timestampLog() + msg)
