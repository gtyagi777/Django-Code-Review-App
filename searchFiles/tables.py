import django_tables2 as tables
from .models import FileTable
from django.utils.html import format_html

class PTable(tables.Table):
    FileName = tables.Column()
    Extension = tables.Column()
    Path_File = tables.Column(empty_values=())

    def render_Path_File(self,record):
        x = str(record.RootPath)
        return format_html("<a href=\"displayFile/" + str(record.FileID) + "\">Visit File</a>")

    class Meta:
        model = FileTable
        template_name = 'django_tables2/semantic.html'
