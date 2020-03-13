from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Posts', views.postViewSet)

urlpatterns = [
    path('', views.hero, name='hero'),
    path('post/<int:id>/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('postComment/', views.coment, name='postComment'),
    path('api/', include(router.urls)),
    path('api-app/', include('rest_framework.urls', namespace='rest_framework'))
]
