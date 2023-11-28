# Generated by Django 4.2.7 on 2023-11-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarvelUniverse', '0016_merge_20231128_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]