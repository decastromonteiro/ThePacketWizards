# todo: create share buttons for each blogspot
# todo: create related posts
# todo: create search feature
# todo: implement Celery to post to twitter when an article is available
from .celery import app as celery_app

__all__ = ("celery_app",)
