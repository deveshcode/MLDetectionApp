# -*- coding: utf-8 -*-
"""MLOD backend module"""
from flasgger import Swagger # for flasgger
from flask import Flask # for flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware # for setting context path
from .config import config # for getting flask url from
from .views import PredictView

# define flask application
# pylint: disable=invalid-name, too-many-format-args
application = Flask(__name__)

# pylint: disable=unused-argument
def simple(env, resp):
    """Method that returns invalid url"""
    resp(b"200 OK", [(b"Content-Type", b"text/plain")])
    return [b"Please re-verify the URL. Check if context path is present"]

# this is defining the app with context path
application.wsgi_app = DispatcherMiddleware(
    simple, {config.get("flask", "base_url"): application.wsgi_app}
)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "ML Object Detector",
        "description": "REST API's for interacting with backend",
        "version": "1.0.0",
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "backend",
            "route": "/docs/backend.json".format(config.get("flask", "base_url")),
        }
    ],
    "static_url_path": "/flasgger_static".format(config.get("flask", "base_url")),
    "swagger_ui": True,
    "specs_route": "/docs".format(config.get("flask", "base_url")),
    "basePath": "/mlod/api",
}

swag = Swagger(application, config=swagger_config, template=swagger_template)

#register apis
application.add_url_rule(
    "/v1/predict",
    view_func=PredictView.as_view("Predict_lc"),
    methods=["POST"],
)