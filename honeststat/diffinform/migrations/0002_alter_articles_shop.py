# Generated by Django 4.2.3 on 2023-08-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diffinform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='shop',
            field=models.TextField(blank=True, null=True),
        ),
    ]