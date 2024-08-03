#!/usr/bin/env python3
"""
    Index view for the API.
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON status."""
    return jsonify({"status": "OK"})

