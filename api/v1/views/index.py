#!/usr/bin/python3
from flask import Blueprint, jsonify
from models import storage

stats_blueprint = Blueprint('stats',__name__)
@stats_blueprint.route('/api/v1/stats', method=['GET'])
def get_stats():
    object_counts = storage.count()
    return jsonify(object_counts)

