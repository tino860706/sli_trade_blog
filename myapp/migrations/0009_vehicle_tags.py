# Generated by Django 3.2.6 on 2021-08-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210815_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]