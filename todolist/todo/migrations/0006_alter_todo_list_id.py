# Generated by Django 5.0.6 on 2024-06-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
