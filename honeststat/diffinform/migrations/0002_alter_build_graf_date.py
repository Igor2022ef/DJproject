# Generated by Django 4.2.3 on 2023-08-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diffinform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build_graf',
            name='date',
            field=models.CharField(blank=True, default=0, max_length=150),
            preserve_default=False,
        ),
    ]