# Generated by Django 4.0.4 on 2022-05-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelinherit', '0002_book_book_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('book_price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='book_info',
            name='book_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelinherit.book'),
        ),
        migrations.CreateModel(
            name='book_price',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('modelinherit.book_lang',),
        ),
    ]
