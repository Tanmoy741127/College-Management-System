# Generated by Django 3.0.7 on 2020-10-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201025_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesdata',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
