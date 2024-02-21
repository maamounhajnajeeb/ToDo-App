import multiprocessing
import os
from distutils.util import strtobool


port, host = os.environ.get("PORT", "8000"), os.environ.get("HOST", "0.0.0.0")
bind = f"{host}:{port}"

accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(M)sms"  # noqa: E501

# workers = int(os.environ.get("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
workers = int(os.environ.get("WEB_CONCURRENCY", multiprocessing.cpu_count() ))
threads = int(os.environ.get("PYTHON_MAX_THREADS", 1))

reload = bool(strtobool(os.environ.get("WEB_RELOAD", "false")))
