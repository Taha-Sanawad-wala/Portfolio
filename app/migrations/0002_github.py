# Generated by Django 4.1.7 on 2023-04-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='app/uploads')),
            ],
        ),
    ]
