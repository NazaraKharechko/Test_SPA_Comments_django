from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
        path('', login_required(views.create_comment), name='home'),
        path('login/', views.user_login, name='login'),
        path('signup/', views.signup, name='signup'),
        path('logout/', views.logout_view, name='logout'),

]
