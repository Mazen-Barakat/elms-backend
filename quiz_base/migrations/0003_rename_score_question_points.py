# Generated by Django 4.1.7 on 2023-03-18 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_base', '0002_rename_quiz_quizmodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='score',
            new_name='points',
        ),
    ]
