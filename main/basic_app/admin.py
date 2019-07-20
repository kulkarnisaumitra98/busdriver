from django.contrib import admin
from .models import Trackie, Tracker, PolyLine, Busdriver
# Register your models here.

admin.site.register(Tracker)
admin.site.register(Trackie)
admin.site.register(PolyLine)
admin.site.register(Busdriver)
