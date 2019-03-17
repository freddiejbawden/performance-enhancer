class LightThing:
  
  TYPE = "LIGHT"

  def __init__(self, id, address, levels, level):
    self.type = LightThing.TYPE
    self.id = id
    self.address = address
    self.levels = levels
    self.level = level

  def get_type(self):
    return self.type

  def get_id(self):
    return self.id

  def get_address(self):
    return self.address

  def get_levels(self):
    return self.levels

  def get_level(self):
    return self.level

  def set_level(level):
    self.level = level

  def to_json(self):
    return {'type':self.type, 'id':self.id, 'address':self.address, 'level':self.level, 'levels':self.levels}

  def from_json(thing_json, thing_id):
    address = thing_json['address']
    level = thing_json['level']
    levels = thing_json['levels']
    return LightThing(thing_id, address, levels, level)
