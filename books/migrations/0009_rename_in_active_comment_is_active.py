# Generated by Django 4.0.4 on 2022-05-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_comment_in_active_comment_recommend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='in_active',
            new_name='is_active',
        ),
    ]
