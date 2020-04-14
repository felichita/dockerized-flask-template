from flask import Blueprint, Response
from prometheus_client import multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Gauge, Counter

IN_PROGRESS = Gauge("inprogress_requests", "Example gauge", multiprocess_mode='livesum')
main = Blueprint('main', __name__)

NUM_REQUESTS = Counter("num_requests", "Example counter")

@main.route('/')
@IN_PROGRESS.track_inprogress()
def index():
    NUM_REQUESTS.inc()
    return "Hello, world!"

@main.route('/metrics')
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)
