# Generated by Django 2.2.1 on 2019-06-11 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathTable',
            fields=[
                ('PathID', models.AutoField(primary_key=True, serialize=False)),
                ('Path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TempTable',
            fields=[
                ('FileID', models.AutoField(primary_key=True, serialize=False)),
                ('SearchTerm', models.CharField(max_length=250)),
                ('FileName', models.CharField(max_length=250)),
                ('lineNumber', models.CharField(max_length=50)),
                ('CodeLine', models.CharField(max_length=1000)),
                ('RootPath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_cmp.PathTable')),
            ],
        ),
        migrations.CreateModel(
            name='FileTable',
            fields=[
                ('FileID', models.AutoField(primary_key=True, serialize=False)),
                ('FileName', models.CharField(max_length=250)),
                ('Extension', models.CharField(max_length=50)),
                ('RootPath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_cmp.PathTable')),
            ],
        ),
    ]
