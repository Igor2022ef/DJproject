# Generated by Django 4.2.3 on 2023-08-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diffinform', '0004_alter_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название товара'),
        ),
    ]
