from django.contrib import admin
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register('pasazerowie',.views.PasazerowieView)

app_name = 'RezerwacjeApp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect),
    path('wybor_lotu/<int:id>/pasazer', views.pasazer, name='lot'),
    path('rezerwacje/',views.rezerwacje,name='rezerwacje'),
    path('<int:id>/rezerwacje/',views.rezerwacje,name='rezerwacje'),
    path('wybor_lotu/',views.wybor_lotu,name='wybor_lotu')
]