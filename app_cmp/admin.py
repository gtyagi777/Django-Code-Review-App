from django.contrib import admin

# Register your models here.
from .models import PathTable, FileTable

admin.site.register(PathTable)
admin.site.register(FileTable)
