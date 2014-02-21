from flask import json
from flask import Response

def returnJson(obj):
    return Response(json.dumps(obj), content_type='application/json; charset=utf-8')