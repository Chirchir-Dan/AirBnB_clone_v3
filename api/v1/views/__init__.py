#!/usr/bin/env python3
"""
    Initialize the Blueprint for the views.
"""


from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views import index
# Wildcard import of everything in the package api.v1.views.index
# PEP8 will complain about it, don’t worry, it’s normal and this file
# (v1/views/__init__.py) won’t be checked.
