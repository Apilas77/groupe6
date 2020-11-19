# Generated by Django 3.0.5 on 2020-11-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(error_messages={'unique': 'An application with that name already exists.'}, max_length=128, unique=True)),
                ('active', models.BooleanField(default=False, help_text='Avoid any errors before the apps has been ready')),
            ],
        ),
    ]
