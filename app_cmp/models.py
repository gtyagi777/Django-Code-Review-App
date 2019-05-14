from django.db import models

class TempTable(models.Model):
    FileID = models.AutoField(primary_key=True)
    RootPath = models.CharField(max_length=1000)
    FileName = models.CharField(max_length=250)
    lineNumber = models.CharField(max_length=50)

    def __str__(self):
        return self.FileName
