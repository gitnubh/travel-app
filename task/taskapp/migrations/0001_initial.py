# Generated by Django 4.2.7 on 2023-11-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='screenshots')),
                ('description', models.TextField()),
            ],
        ),
    ]