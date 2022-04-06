from masonite.routes import Route
# commented out for testing routes
# from masonite.authentication import Auth
from app.controllers.auth.RegisterController import RegisterController
from app.controllers.auth.LoginController import LoginController

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/blog", "BlogController@show"),
    Route.get("/login", LoginController.show).name('login'),
    Route.post("/login", LoginController.store).name('login.store'),
    Route.get("/logout", LoginController.logout).name('logout'),
    Route.get("/register", RegisterController.show).name('register'),
    Route.post("/register", RegisterController.store).name('register.store'),
    ]

# Manually add routes from auth module
# ROUTES += Auth.routes()