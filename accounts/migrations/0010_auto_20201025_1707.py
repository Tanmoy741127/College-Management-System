# Generated by Django 3.0.7 on 2020-10-25 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notes',
            new_name='notesData',
        ),
    ]
