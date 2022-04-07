from masonite.routes import Route
# commented out for testing routes
from masonite.authentication import Auth
from app.controllers.auth.RegisterController import RegisterController
from app.controllers.auth.LoginController import LoginController

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/blog", "BlogController@show"),
    Route.post('/blog/create', 'BlogController@store')
    ]

# Manually add routes from auth module
ROUTES += Auth.routes()