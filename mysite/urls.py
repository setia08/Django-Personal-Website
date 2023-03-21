from django.conf import settings
from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path("",views.index,name="index"),
    path("about_me",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("login",views.login_view,name="login"),
path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
path("register",views.register,name="register"),
path("client",views.client,name="client"),
path("add_project",views.add_project,name="add_project"),
path("view_projects",views.view_project,name="view_project")
]

