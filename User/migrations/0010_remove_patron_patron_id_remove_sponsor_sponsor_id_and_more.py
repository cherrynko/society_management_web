# Generated by Django 4.0.8 on 2022-12-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_sponsor_patron'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='patron',
        #     name='patron_id',
        # ),
        # migrations.RemoveField(
        #     model_name='sponsor',
        #     name='sponsor_id',
        # ),
        migrations.AddField(
            model_name='patron',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assistantdirector',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='director',
            name='email_id',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ec',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
