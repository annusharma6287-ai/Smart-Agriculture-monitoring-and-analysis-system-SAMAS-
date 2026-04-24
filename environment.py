class environment:
    def __init__(self,temperature,humidity,rainfall_index):
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall_index = rainfall_index
    def update_environment(self,temperature,humidity,rainfall):
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall_index = rainfall
    def to_dict(self):
        return {
            "temperature":self.temperature,
            "humidity":self.humidity,
            "rainfall_index":self.rainfall_index
        }