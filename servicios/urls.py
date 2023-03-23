from django.urls import path
from servicios import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.servicios, name='servicios')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)