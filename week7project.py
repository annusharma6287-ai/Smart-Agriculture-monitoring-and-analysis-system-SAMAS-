from datetime import datetime
class record:
    def __init__(self,date):
        self.date = date
        self.timestamp = datetime.now()
    def get_date(self):
        return self.date
    def get_timestamp(self):
        return self.timestamp
