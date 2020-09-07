from api_python.database import db
from api_python.routes import auth

from werkzeug.exceptions import HTTPException
import os
from flask import Flask, json


def create_app(test_config=None):
    """Application factory function

    Parameters
    ----------
    test_config : object
        Object with the configuration you want the app launched

    Returns
    -------
    Flask
        The app instance
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api_python.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # test api
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # init db
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth.bp)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    return app
