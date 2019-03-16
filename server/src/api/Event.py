from Action import Action


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

  def to_json(self):
    return {'id':self.id, 'name':self.name, 'trigger':self.trigger, 'actions':[ action.to_json() for action in self.actions ]}

  def from_json(event_json, id=None):
    id = id or event_json['id']
    name = event_json['name']
    trigger = event_json['trigger']
    actions = [ Action.from_json(action_json) for action_json in event_json['actions'] ]
    return Event(id, name, trigger, actions)
