from django.urls import path,include
from rest_framework import routers
from Tasks import views

#api versioning
router = routers.DefaultRouter()
router.register(r'Tasks', views.TaskView, 'Tasks')


urlpatterns = [
  path("api/v1/", include(router.urls))  
]
