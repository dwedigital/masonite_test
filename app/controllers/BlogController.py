from masonite.views import View
from masonite.controllers import Controller
from app.models.Post import Post
from masonite.request import Request

class BlogController(Controller):
    """BlogController Controller Class."""

    def show(self, view: View):
        print("test")
        return view.render("blog")

    def store(self, req: Request):
        Post.create(
            title=req.input('title'),
            body=req.input('body'),        
            author_id=req.user().id
        )
        return 'Post Created'