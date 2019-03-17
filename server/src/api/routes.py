from api import api
from flask import abort
import json

from IDGenerator import IDGenerator


 # Things API

things = dict()

thing_id_gen = IDGenerator(0)

def thing_from_json(thing_json):
  type = request.json['type']
  if (type == LightThing.TYPE):
    id = thing_id_gen.next()
    thing = LightThing.from_json(request.json, id)
    things[id] = thing
  elif (type == SwitchThing.TYPE):
   id = thing_id_gen.next()
   thing = SoundThing.from_json(request.json, id)
   things[id] = thing
  else:
    raise RuntimeError



# Thing API


@api.route('/api/things', methods=['GET'])
def get_things():
  return json.dumps([ thing.to_json() for thing in things])

@api.route('/api/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  return json.dumps(things[thing_id].to_json())

@api.route('/api/things', methods=['POST'])
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


@api.route('/api/things/<int:thing_id>', methods=['DELETE'])
def delete_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  things.pop(thing_id)
  return json.dumps({'result':True})



# LightThing-specific API


@api.route('/api/things/<int:thing_id>/level', methods=['GET'])
def get_thing_level(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != LightThing.TYPE):
    abort(404)
  return json.dumps({'level':thing.get_level()})

@api.route('/api/things/<int:thing_id>/level', methods=['PUT'])
def update_thing_level(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != LightThing.TYPE):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    level = request.json['level']
    things[thing_id].set_level(level)
  except:
    abort(400)
  return json.dumps({'result':True})

@api.route('/api/things/<int:thing_id>/levels', methods=['GOT'])
def get_thing_levels(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != LightThing.TYPE):
    abort(404)
  return json.dumps({'levels':thing.get_levels()})



# SwitchThing-specific API


@api.route('/api/things/<int:thing_id>/on', methods=['GET'])
def get_thing_on(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != SwitchThing.TYPE):
    abort(404)
  return json.dumps({'on':thing.get_on()})

@api.route('/api/things/<int:thing_id>/on', methods=['PUT'])
def update_thing_on(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != SwitchThing.TYPE):
    abort(404)
  if (not request.json):
    abort(400)
  try:
    on = request.json['on']
    things[thing_id].set_on(on)
  except:
    abort(400)
  return json.dumps({'result':True})
