# Generated by Django 2.0.2 on 2018-06-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall', '0009_auto_20180601_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['occupation_start_date']},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['start_chainage']},
        ),
    ]