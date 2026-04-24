from record import record
class farm_log(record):
    def __init__(self,date,crop,soil,environment):
        self.date = date
        self.crop = crop
        self.soil = soil
        self.environment = environment
    def summary(self):
        return {
            "date": self.get_date(),
            "crop": self.crop,
            "soil": self.soil,
            "moisture": self.moisture,
            "height": self.height
        }
    def __str__(self):
        return f"Farm_log(Date = {self.get_date()},crop = {self.crop_name})"
