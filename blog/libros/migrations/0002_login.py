# Generated by Django 3.1.7 on 2021-03-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=40)),
                ('contra', models.CharField(max_length=60)),
            ],
        ),
    ]
