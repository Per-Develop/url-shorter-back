import imp
from django.urls import path
from main import views
from .views import AddrListApiView


urlpatterns = [
    path('api/<value>', AddrListApiView.as_view()),
    path('api', AddrListApiView.as_view()),
    path('test', views.fetch),
    path('<value>', views.index)
]