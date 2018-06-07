# Generated by Django 2.0.2 on 2018-06-07 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_noi', models.PositiveIntegerField()),
                ('system_line', models.CharField(help_text='Enter the System Line e.g. Sunbury to Bendigo.', max_length=100)),
                ('occupation_start_date', models.DateTimeField(help_text='Format is YYYY-MM-DD HH-MM-SS')),
                ('occupation_end_date', models.DateTimeField(help_text='Format is YYYY-MM-DD HH-MM-SS')),
                ('occupation_type', models.CharField(help_text='Enter the Occupation Type e.g. BLU', max_length=50)),
                ('rail_area', models.CharField(choices=[('Western Region', 'Western Region'), ('North/North-East Region', 'North/North-East Region'), ('Central & Eastern Region', 'Central & Eastern Region')], help_text='Enter the Rail Area Type e.g. North/North-East', max_length=50)),
            ],
            options={
                'ordering': ['occupation_start_date'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_chainage', models.DecimalField(decimal_places=3, max_digits=6)),
                ('end_chainage', models.DecimalField(decimal_places=3, max_digits=6)),
                ('discipline', models.CharField(choices=[('Civil', 'Civil'), ('Track', 'Track'), ('Facilities', 'Facilities'), ('Signals', 'Signals')], help_text='Enter the discipline e.g. Civil', max_length=100)),
                ('work_information', models.CharField(max_length=255)),
                ('additional_details', models.CharField(blank=True, max_length=255)),
                ('works_start_date', models.DateField(help_text='Format is YYYY-MM-DD')),
                ('works_end_date', models.DateField(help_text='Format is YYYY-MM-DD')),
                ('occupation_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_wall.Occupation')),
            ],
            options={
                'ordering': ['start_chainage'],
            },
        ),
    ]
