# Generated by Django 3.0.7 on 2020-10-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20201025_2252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='marksData',
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='evaluated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='marks',
            field=models.BigIntegerField(null=True),
        ),
    ]
