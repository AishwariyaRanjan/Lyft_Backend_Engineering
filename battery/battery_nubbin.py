from battery import Battery
from datetime import datetime


class Nubbin(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if threshold_date < self.current_date:
            return True
        else:
            return False
