""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Post(Model):
    """Post Model"""
    fillable = ["title", "author_id", "body"]

    @belongs_to("author_id", "id")
    def author(self):
        from app.models.User import User
        return User