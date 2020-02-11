from django.contrib import admin
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register('pasazerowie',.views.PasazerowieView)

app_name = 'RezerwacjeApp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pasazer/', views.pasazer, name='pasazer'),
    path('siedzenia/<pasazer_id>/<lot>', views.siedzenia, name='siedzenia')
]