# Generated by Django 3.2.2 on 2021-05-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='filename',
            field=models.CharField(default='not set', max_length=200),
        ),
        migrations.AddField(
            model_name='piece',
            name='publisher',
            field=models.CharField(default='not set', max_length=200),
        ),
        migrations.AlterField(
            model_name='piece',
            name='composer',
            field=models.CharField(default='not set', max_length=200),
        ),
        migrations.AlterField(
            model_name='piece',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a> (if unknown, enter "unknown")', max_length=13, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='title',
            field=models.CharField(default='not set', max_length=200),
        ),
    ]
