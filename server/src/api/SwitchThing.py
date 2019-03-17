class SwitchThing:

  TYPE = "SWITCH"

  def __init__(self, id, address, on):
    self.type = SwitchThing.TYPE
    self.id = id
    self.address = address
    self.on = on

  def get_type(self):
    return self.type

  def get_id(self):
    return self.id

  def get_address(self):
    return self.address

  def get_on(self):
    return self.on

  def set_on(self, on):
    self.on = on

  def to_json(self):
    return {'type':self.type, 'id':self.id, 'address':self.address, 'on':self.on}

  def from_json(thing_json, thing_id):
    address = thing_json['address']
    on = thing_json['on']
    return SwitchThing(thing_id, address, on)
    
