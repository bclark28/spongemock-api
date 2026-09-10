"""Application factory for spongemock-api."""

from flask import Flask

from spongemock_api.routes import api


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
