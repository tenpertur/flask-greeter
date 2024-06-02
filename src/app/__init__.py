import os
from flask import Flask
from prometheus_client import start_http_server
from .views import bp as main_bp

def create_app():
    app = Flask(__name__)

    # Configuration from environment variables
    PORT = int(os.getenv('PORT', 2000))
    METRICS_PORT = int(os.getenv('METRICS_PORT', 8008))

    app.register_blueprint(main_bp)

    # start_http_server(METRICS_PORT)  # Start Prometheus metrics server on the specified port

    return app, PORT

