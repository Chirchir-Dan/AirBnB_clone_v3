#!/usr/bin/python3
"""
    This is the main application file for the Flask app.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register the blueprint1
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Handle the teardown of the app context and close
    storage."""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_PORT', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
