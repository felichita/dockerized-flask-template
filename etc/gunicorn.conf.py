# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os
import multiprocessing

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))
_ETC = os.path.join(_ROOT, 'etc')

loglevel = os.getenv('LOG_LEVEL')
# errorlog = os.path.join(_VAR, 'log/api-error.log')
# accesslog = os.path.join(_VAR, 'log/api-access.log')
errorlog = "-"
accesslog = "-"

# bind = 'unix:%s' % os.path.join(_VAR, 'run/gunicorn.sock')
bind = f"0.0.0.0:{os.getenv('GUNICORN_PORT')}"
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True
