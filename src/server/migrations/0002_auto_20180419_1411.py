# Generated by Django 2.0.4 on 2018-04-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Moderator_Id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='Status_id',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='StatusType',
        ),
        migrations.DeleteModel(
            name='UdvUser',
        ),
    ]
