# Generated by Django 4.1.4 on 2023-01-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]