from django.db import models

# Create your models here.


class PathTable(models.Model):
    PathID = models.AutoField(primary_key=True)
    Path = models.TextField()

    def __str__(self):
        return self.Path


class FileTable(models.Model):
    FileID = models.AutoField(primary_key=True)
    RootPath = models.ForeignKey(PathTable, on_delete=models.PROTECT)
    FileName = models.CharField(max_length=250)
    Extension = models.CharField(max_length=50)

    def __str__(self):
        return self.FileName
