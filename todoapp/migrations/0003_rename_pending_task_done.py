# Generated by Django 3.2.4 on 2021-06-27 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_strk_task_pending'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='pending',
            new_name='done',
        ),
    ]
