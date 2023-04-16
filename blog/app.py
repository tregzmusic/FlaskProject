from time import time

from flask import Flask, g
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return f'Hello, {request.method}!'


@app.before_request
def process_before_request():
    g.start_time = time()


@app.after_request
def process_after_request(response):
    if hasattr(g, 'start_time'):
        response.headers['process_time'] = time() - g.start_time
    return response


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return '404'
