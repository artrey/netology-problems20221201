# Generated by Django 4.1.3 on 2022-12-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_rename_is_favourite_note_favourite_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="is_private",
            field=models.BooleanField(default=True),
        ),
    ]
