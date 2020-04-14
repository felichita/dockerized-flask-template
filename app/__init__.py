from flask import Flask

from healthcheck import HealthCheck
from .main import main as main_blueprint

app = Flask(__name__)

# Register routes:
app.register_blueprint(main_blueprint)
#app.register_blueprint(metrics_blueprint)

health = HealthCheck()
app.add_url_rule("/health_check", "healthcheck", view_func=lambda: health.run())
