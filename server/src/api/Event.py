class Event:

  def __init__(self, id, name, trigger, actions):
    self.id = id
    self.name = name
    self.trigger = trigger
    self.actions = actions

  def get_id():
    return self.id

  def get_name():
    return self.name

  def get_trigger():
    return self.trigger

  def get_actions():
    return self.actions
