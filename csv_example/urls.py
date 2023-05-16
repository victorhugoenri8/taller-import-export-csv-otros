

from django.contrib import admin
from django.urls import path

from core.views import export_csv, import_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', export_csv),
    path('import/', import_csv),
]
