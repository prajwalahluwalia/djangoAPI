# Generated by Django 4.0.4 on 2022-06-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
