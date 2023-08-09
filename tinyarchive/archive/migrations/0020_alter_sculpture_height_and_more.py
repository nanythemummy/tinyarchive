# Generated by Django 4.0.5 on 2023-08-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0019_alter_sculpture_installed_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sculpture',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sculpture',
            name='installed_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sculpture',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sculpture',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sculpture',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
