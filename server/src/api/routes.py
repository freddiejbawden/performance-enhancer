from api import api
import json


@api.route('/')
@api.route('/api')
def root():
  return "Hello, World!"

@api.route('/api/events', methods=['GET']):
def get_events():
  return json.dumps([])

@api.route('/api/events/<int:id>', methods=['GET'])
def get_event(id):
  return json.dumps({})

@api.route('/api/events', methods=['POST']):
def make_event():
  return json.dumps({}), 201

@api.route('/api/events/<int:id>', methods=['PUT']):
def update_event(id):
  return json.dumps({})

@api.route('/api/events/<int:id>', methods=['DELETE']):
def delete_event(id):
  return json.dumps({'result':True})  
