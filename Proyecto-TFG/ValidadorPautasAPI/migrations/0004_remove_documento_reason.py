# Generated by Django 4.0.4 on 2022-05-16 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ValidadorPautasAPI', '0003_alter_documento_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='reason',
        ),
    ]
