# Generated by Django 5.0.6 on 2024-06-26 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_list_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_list',
            new_name='todo_lists',
        ),
    ]
