from masonite.views import View
from masonite.controllers import Controller

class BlogController(Controller):
    """BlogController Controller Class."""

    def show(self, view: View):
        print("test")
        return view.render("blog")