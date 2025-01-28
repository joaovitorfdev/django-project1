from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipes'

urlpatterns = [
    path('',  views.home, name='home'),
    path('recipes/<int:id>/',  views.recipe, name='recipe'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

