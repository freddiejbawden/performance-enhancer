from api import api
from flask import abort
import json

from IDGenerator import IDGenerator


# Dictionary of shows

shows = dict()


# Path to shows file

SHOWS_PATH = "shows.json"


# Reads shows from a JSON file

def read_shows():
  try:
    with open(SHOWS_PATH, "r") as f:
      show_list = [ Show.from_json(show_json) for show_json in json.load(f) ]
      shows = dict([ (show.get_id(), show) for show in show_list ])
  except IOError:
    print("Unable to read shows from file")
    raise RuntimeError


# Writes shows into a JSON file

def write_shows():
  try:
    with open(SHOWS_PATH, "w") as f:
      f.write([ show.to_json() for show in shows.values() ])
  except IOError:
    print("Unable to write shows to file")
    raise RuntimeError


# Read shows from file

read_shows()


# Show ID generator

if (len(shows) > 0):
  show_id_gen = IDGenerator(max(shows) + 1)
else:
  show_id_gen = IDGenerator(0)
  


def show_exists(show_id):
  return show_id in shows

def event_exists(show_id, event_id):
  return show_exists and event_id in shows[show_id].get_events()

# Show API

@api.route('/api/shows', methods=['GET'])
def get_shows():
  return json.dumps([ show.to_json() for show in shows.values() ])

@api.route('/api/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
  if (show_exists(show_id)):
    return json.dumps(shows[show_id].to_json())
  abort(404)

@api.route('/api/shows', methods=['POST'])
def make_show():
  if (not request.json):
    abort(400)
  try:
    show = Show.from_json(request.json, show_id_gen.next())
    shows.append(show)
    return json.dumps(show.to_json()), 201
  except:
    abort(400)

@api.route('/api/shows/<int:show_id>', methods=['PUT'])
def update_show(show_id):
  if (not show_exists(show_id)):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    show = Show.from_json(request.json, show_id)
    shows[show_id] = show
    return json.dumps(show.to_json())
  except:
    abort(400)

@api.route('/api/shows/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
  if (not show_exists(show_id)):
    abort(404)
  shows.pop(show_id)
  return json.dumps({'result':True})


# Event API

@api.route('/api/shows/<int:show_id>/events', methods=['GET'])
def get_events(show_id):
  if (not show_exists(show_id)):
    abort(404)
  show = shows[show_id]
  return json.dumps(show.get_events().to_json())

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['GET'])
def get_event(show_id, event_id):
  if (not event_exists(show_id, event_id)):
    abort(404)
  event = shows[show_id].get_events()[event_id]
  return json.dumps(event.to_json())

@api.route('/api/shows/<int:show_id>/events', methods=['POST'])
def make_event(show_id):
  if (not show_exists(show_id)):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    show = shows[show_id]
    event = show.add_event_from_json(request.json)
    return json.dumps(event.to_json())
  except:
    abort(400)

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['PUT'])
def update_event(show_id, event_id):
  if (not event_exists(show_id, event_id)):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    show = shows[show_id]
    event = Event.from_json(request.json, event_id)
    show.update_event(event)
    return json.dumps(event.to_json())
  except:
    abort(400)

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['DELETE'])
def delete_event(show_id, event_id):
  if (not event_exists(show_id, event_id)):
    shows[show_id].remove_event(event_id)
  return json.dumps({'result':True})
