from django import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]