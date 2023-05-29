# Generated by Django 2.1.7 on 2023-05-21 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('low_bound', models.DecimalField(decimal_places=2, max_digits=5)),
                ('up_bound', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=10)),
                ('pname', models.CharField(max_length=10)),
                ('h', models.IntegerField()),
                ('w', models.IntegerField()),
            ],
        ),
    ]
