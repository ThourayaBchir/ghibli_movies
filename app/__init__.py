from flask import Flask
from flask_caching import Cache

config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 60
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

from app import routes  # noqa: E402, F401
