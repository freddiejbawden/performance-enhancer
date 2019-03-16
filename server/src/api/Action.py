class Action:

  def __init__(self, id, type, options):
    self.id = id
    self.type = type
    self.options = options

  def get_id(self):
    return self.id

  def get_type(self):
    return self.type

  def get_options(self):
    return self.options

  def to_json(self):
    return {'id':self.id, 'type':self.type, 'options':self.options}

  def from_json(action_json, id=None):
    id = id or action_json['id']
    type = action_json['type']
    options = action_json['options']
    return Action(id, type, options)
