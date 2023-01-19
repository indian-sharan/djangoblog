from django.urls import path
#from . import views
from .views import HomeView, ArticleView, AddPost

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<slug>', ArticleView.as_view(), name='articleview'),
    path('addpost/', AddPost.as_view(), name='addpost'),
]
