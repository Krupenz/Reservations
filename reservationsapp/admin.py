from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Rezerwacje)
admin.site.register(Trasy)
admin.site.register(Pasazerowie)
admin.site.register(Siedzenia)
admin.site.register(Lotniska)
admin.site.register(Loty)
admin.site.register(Samoloty)

admin.site.site_header = "Adison Airlines"
