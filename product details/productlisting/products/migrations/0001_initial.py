# Generated by Django 4.2.6 on 2023-12-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(max_length=20)),
                ('description', models.TextField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]