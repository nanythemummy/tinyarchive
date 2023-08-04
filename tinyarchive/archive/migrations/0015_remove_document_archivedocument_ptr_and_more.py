# Generated by Django 4.0.5 on 2023-08-03 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0014_artifact_designer_artifact_installed_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='archivedocument_ptr',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='archivedocument_ptr',
        ),
        migrations.DeleteModel(
            name='AudioRecording',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Photograph',
        ),
    ]
