# Generated by Django 4.1.7 on 2023-03-18 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_randomizedquestion_randomquestion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'quizzes'},
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='score',
        ),
    ]
