#!/usr/bin/python3
"""is the index for app api @author: @medjarraya"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """ returns dictionary containing status """
    return jsonify({'status': "OK"})


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """ returns dictionary with classes and their count"""
    classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    countDict = {}
    for objType, cls in classes.items():
        countDict.update({objType: storage.count(cls)})
    return jsonify(countDict)
