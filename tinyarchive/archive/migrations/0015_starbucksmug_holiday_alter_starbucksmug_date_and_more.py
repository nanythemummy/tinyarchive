# Generated by Django 4.0.5 on 2022-08-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0014_starbucksmug_color_starbucksmug_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='starbucksmug',
            name='holiday',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='starbucksmug',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='starbucksmug',
            name='productionLocation',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='starbucksmug',
            name='shapeDescription',
            field=models.TextField(),
        ),
    ]
