# Generated by Django 5.0.1 on 2024-01-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloapedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('category', models.CharField(choices=[('Fashion', 'Fashion'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Food', 'Food'), ('Health', 'Health')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]