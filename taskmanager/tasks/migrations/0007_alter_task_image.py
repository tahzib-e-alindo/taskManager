# Generated by Django 5.0.1 on 2024-02-05 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_options_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='task_images'),
        ),
    ]
