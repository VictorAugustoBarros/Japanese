from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ListProductView

app_name = "words"

urlpatterns = [
    path("", ListProductView.as_view(), name="home"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
