# Generated by Django 2.0.5 on 2020-03-25 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200325_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published',
        ),
    ]
