# Generated by Django 4.0.8 on 2022-12-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_remove_patron_patron_id_remove_sponsor_sponsor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patron',
            old_name='member_id',
            new_name='patron_id',
        ),
    ]
