# Generated by Django 4.0.4 on 2022-05-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='state_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
