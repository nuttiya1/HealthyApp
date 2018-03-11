# Generated by Django 2.0.1 on 2018-03-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitjang', '0004_auto_20180224_1713'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
        migrations.AddField(
            model_name='activity',
            name='amount_of_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='weight_data',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
