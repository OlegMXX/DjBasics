# Generated by Django 4.1.1 on 2022-10-15 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_bode_as_markdown_news_body_as_markdown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='create_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='update_date',
            new_name='updated',
        ),
    ]
