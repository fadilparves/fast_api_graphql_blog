from orator import has_many
from db import Model

class User(Model):
    @has_many #This is to describe that one user has many posts and comments
    def posts(self):
        from .post import Post

        return Post

    @has_many
    def comments(self):
        from .comment import Comments

        return Comments
