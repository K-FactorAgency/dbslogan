from django.urls import path
from .views import IndexView, RegisterView, LoginView, LogoutView, CreatePostView, DeletePostView, LikePostView

app_name = 'nemo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('like_post/<int:pk>/', LikePostView.as_view(), name='like_post'),
]
