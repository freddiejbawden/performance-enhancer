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
