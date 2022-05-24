# Generated by Django 4.0.4 on 2022-05-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelinherit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='book_info',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelinherit.book')),
                ('author_name', models.CharField(max_length=50)),
            ],
            bases=('modelinherit.book',),
        ),
    ]
