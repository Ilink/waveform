from flask import json
from util import *
from flask import Flask
from flask import jsonify
from flask import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/buoys")
def getAllBuoys():
    return returnJson(["buoy1", "buoy2"])

@app.route("/buoys/<int:buoyId>")
def getBuoy(buoyId):
    return returnJson(["buoy%d" % buoyId])

if __name__ == "__main__":
    app.run(debug=True)