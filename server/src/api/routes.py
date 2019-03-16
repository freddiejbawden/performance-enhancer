from api import api
import json


@api.route('/')
@api.route('/api')
def root():
  return "Hello, World!"


# Show API

@api.route('/api/shows', methods=['GET'])
def get_shows():
  return json.dumps([])

@api.route('/api/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
  return json.dumps({})

@api.route('/api/shows', methods=['POST'])
def make_show():
  return json.dumps({}), 201

@api.route('/api/shows/<int:show_id>', methods=['PUT'])
def update_show(show_id):
  return json.dumps({})

@api.route('/api/shows/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
  return json.dumps({'result':True})


# Event API

@api.route('/api/shows/<int:show_id>/events', methods=['GET'])
def get_events(show_id)
  return json.dumps([])

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['GET'])
def get_event(show_id, event_id):
  return json.dumps({})

@api.route('/api/shows/<int:show_id>/events', methods=['POST'])
def make_show(show_id):
  return json.dumps({}), 201

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['PUT'])
def update_show(show_id, event_id):
  return json.dumps({})

@api.route('/api/shows/<int:show_id>/events/<int:event_id>', methods=['DELETE'])
def delete_show(show_id, event_id):
  return json.dumps({'result':True})
