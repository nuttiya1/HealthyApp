# Generated by Django 2.0.1 on 2018-03-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitjang', '0008_auto_20180311_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('value', models.FloatField()),
            ],
        ),
    ]