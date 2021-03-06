# Generated by Django 4.0.4 on 2022-05-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValidadorPautasAPI', '0006_remove_documento_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextoAnalizado',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('texto', models.TextField(max_length=500)),
                ('pauta', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='reason',
            field=models.CharField(default='', max_length=300),
        ),
    ]
