# from celery import Celery
from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('project.config.Config')

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
cache = Cache(app)

# celery = Celery(
#     __name__,
#     broker='redis://localhost:6379/0',
#     backend='redis://localhost:6379/0'
# )
