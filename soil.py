class soil:
    def __init__(self,moisture,ph):
        self.moisture = moisture
        self.ph = ph
    def update_moisture(self,new_moisture):
        self.moisture = new_moisture
    def update_ph(self,new_ph):
        self.ph = new_ph
    def to_dict(self):
        return {"moisture":self.moisture,"ph":self.ph}