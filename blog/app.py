from flask import Flask
from blog.report.views import report
from blog.user.views import user

app = Flask(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
