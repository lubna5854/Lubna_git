# Generated by Django 4.2.1 on 2023-06-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_prio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
