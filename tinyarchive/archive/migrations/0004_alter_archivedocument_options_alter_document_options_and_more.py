# Generated by Django 4.0.5 on 2022-06-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_alter_archivedocument_options_alter_document_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivedocument',
            options={},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.AlterModelOptions(
            name='photograph',
            options={},
        ),
        migrations.RenameField(
            model_name='photograph',
            old_name='type',
            new_name='photo_type',
        ),
        migrations.RemoveField(
            model_name='archivedocument',
            name='polymorphic_ctype',
        ),
        migrations.AddField(
            model_name='document',
            name='transcription',
            field=models.TextField(blank=True),
        ),
    ]
