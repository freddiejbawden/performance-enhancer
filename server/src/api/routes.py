from api import *
from api.SwitchThing import SwitchThing
from api.LightThing import LightThing
from flask import abort
from flask import jsonify
from flask import request
import json

from IDGenerator import IDGenerator


 # Things API

things = dict()

thing_id_gen = IDGenerator(0)

def thing_from_json(thing_json):
  type = thing_json['type']
  if (type == LightThing.TYPE):
    id = thing_id_gen.next()
    thing = LightThing.from_json(thing_json, id)
    return thing
  elif (type == SwitchThing.TYPE):
    id = thing_id_gen.next()
    thing = SwitchThing.from_json(thing_json, id)
    return thing
  else:
    print("Invalid type")
    raise RuntimeError



# Thing API


@api.route('/api/things', methods=['GET'])
def get_things():
  return jsonify([ thing.to_json() for thing in things.values()])

@api.route('/api/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  return jsonify(things[thing_id].to_json())

@api.route('/api/things', methods=['POST'])
def register_thing():
  if (not request.json):
    abort(400)
  try:
    thing = thing_from_json(request.json)
    things[thing.get_id()] = thing
    return str(thing.get_id())
  except:
    print("Invalid thing:\n%s" % request.json)
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
    print("Invalid thing:\n%s" % request.json)
    abort(400)


@api.route('/api/things/<int:thing_id>', methods=['DELETE'])
def delete_thing(thing_id):
  if (not thing_id in things):
    abort(404)
  things.pop(thing_id)
  return jsonify({'result':True})



# LightThing-specific API


@api.route('/api/things/<int:thing_id>/level', methods=['GET'])
def get_thing_level(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != LightThing.TYPE):
    abort(404)
  return jsonify({'level':thing.get_level()})

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
  return jsonify({'result':True})

@api.route('/api/things/<int:thing_id>/levels', methods=['GOT'])
def get_thing_levels(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != LightThing.TYPE):
    abort(404)
  return jsonify({'levels':thing.get_levels()})



# SwitchThing-specific API


@api.route('/api/things/<int:thing_id>/on', methods=['GET'])
def get_thing_on(thing_id):
  if (not thing_id in things):
    abort(404)
  thing = things[thing_id]
  if (thing.get_type() != SwitchThing.TYPE):
    abort(404)
  return str((thing.get_on() and 1) or 0)

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
    print("%d set to %b" % (thing_id, on))
  except:
    abort(400)
  return jsonify({'result':True})
