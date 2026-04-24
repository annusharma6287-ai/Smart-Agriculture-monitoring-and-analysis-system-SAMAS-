class crop:
    def __init__(self,name,variety,field,height,stage):
        self.name = name
        self.variety = variety
        self.field = field
        self.height = height
        self.stage = stage
    def update_height(self,new_height):
        self.height = new_height
    def update_stage(self,new_stage):
        self.stage = new_stage
    def to_dict(self):
        return {"name":self.name,"variety":self.variety,"field":self.field,"height":self.height,"stage":self.stage}

