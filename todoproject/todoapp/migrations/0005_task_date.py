# Generated by Django 4.2.1 on 2023-07-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_prio'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
