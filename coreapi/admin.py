from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import PathTable, FileTable, TempTable

admin.site.register(PathTable)
admin.site.register(FileTable)
admin.site.register(TempTable)
