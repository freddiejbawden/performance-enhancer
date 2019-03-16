from Event import Event
from IDGenerator import IDGenerator


class Show:

  def __init__(self, id, name, events):
    self.id = id
    self.name = name
    self.events = events
    self.event_id_gen = IDGenerator(0)
    
  def get_id(self):
    return self.id

  def get_name(self):
    return self.name

  def get_events(self):
    return self.events

  def get_event(self, id):
    if (id in self.events):
      return self.events[id]
    return None

  def add_event_from_json(self, event_json):
    event = Event.from_json(event_json, self.event_id_gen.next())
    self.events[event.get_id()] = event
    return event

  def update_event(self, event):
    if (not event in self.events):
      return None
    self.events[event.get_id()] = event

  def remove_event(self, id):
    if (id in self.events):
      self.events.pop(id)

  def to_json(self):
    return {'id':self.id, 'name':self.name, 'events':[ event.to_json() for event in self.events ]}

  def from_json(show_json, id=None):
    id = id or show_json['id']
    name = show_json['name']
    events = [ Event.from_json(event_json) for event_json in show_json['events'] ]
    return Show(id, name, events)
