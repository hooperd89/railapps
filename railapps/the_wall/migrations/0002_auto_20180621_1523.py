# Generated by Django 2.0.2 on 2018-06-21 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['start_chainage'], 'permissions': (('view_work', 'View Work'),)},
        ),
    ]
