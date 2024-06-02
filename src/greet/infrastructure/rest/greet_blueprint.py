import time
from app.config.logging_config import log_request
from app.config.metrics_config import REQUEST_COUNT, REQUEST_LATENCY
from flask import Blueprint, request, jsonify


greet_bp = Blueprint('greet_blueprint', __name__)

@greet_bp.before_request
def start_timer():
    request.start_time = time.time() 


@greet_bp.after_request
def log_request_data(response):
    request_latency =  time.time() - request.start_time
    REQUEST_LATENCY.labels(request.endpoint).observe(request_latency )
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()

    log_data = {
        'method': request.method,
        'path': request.path,
        'status': response.status_code,
        'response_time': request_latency,
        'ip': request.remote_addr
    }
    log_request(log_data)
    return response

@greet_bp .route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}")
