from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

app_name='proapi'
urlpatterns = [
    path('',views.proapi, name='ProvideAPI'),
    path('emp/',include(router.urls),name='emp'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]