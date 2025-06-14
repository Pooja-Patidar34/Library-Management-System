# Generated by Django 5.1.4 on 2025-06-13 06:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('borrow_date', models.DateField(default=datetime.date.today)),
                ('return_date', models.DateField(default='')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.book')),
            ],
        ),
    ]
