from api import api
from flask import abort
import json

from IDGenerator import IDGenerator


 # Things API

things = dict()

thing_id_gen = IDGenerator(0)

def thing_from_json(thing_json):
  LIGHT_TYPE = "LIGHT"
  SWITCH_TYPE = "SWITCH"

  type = request.json['type']
  if (type == LIGHT_TYPE):
    id = thing_id_gen.next()
    thing = LightThing.from_json(request.json, id)
    things[id] = thing
  elif (type == SWITCH_TYPE):
   id = thing_id_gen.next()
   thing = SoundThing.from_json(request.json, id)
   things[id] = thing
  else:
    raise RuntimeError

@api.route('/api/things', methods=['GET'])
def get_things():
  return json.dumps([ thing.to_json() for thing in things])

@api.route('/api/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  return json.dumps(things[thing_id].to_json())

@api.route('/api/things', methods=['POS'])
def register_thing():
  if (not request.json):
    abort(400)
  try:
    thing = thing_from_json(request.json)
    things[thing.get_id()] = thing
  except:
    print("Invalid thing")
    abort(400)

@api.route('/api/things<int:thing_id>', methods=['PUT'])
def update_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    thing = thing_from_json(request.json)
    things[thing.get_id()] = thing
  except:
    print("Invalid thing format")
    abort(400)


@api.route('/api/shows/<int:thing_id>', methods=['DELETE'])
def delete_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  things.pop(thing_id)
  return json.dumps({'result':True})
