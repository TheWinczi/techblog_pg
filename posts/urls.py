from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from posts import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('posts/<int:id>/', views.post_details, name='post_details'),
    path('posts/create/', views.post_create, name='post_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
