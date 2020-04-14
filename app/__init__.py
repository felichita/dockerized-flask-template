from flask import Flask
from healthcheck import HealthCheck
from prometheus_flask_exporter import PrometheusMetrics

from .main import main as main_blueprint


app = Flask(__name__)
PrometheusMetrics(app)

endpoints = (
    '',
    'health_check',
)

# Register routes:
app.register_blueprint(main_blueprint)

health = HealthCheck()
app.add_url_rule("/health_check", "healthcheck", view_func=lambda: health.run())
