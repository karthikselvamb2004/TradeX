# Generated by Django 5.1.4 on 2025-02-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradexapp', '0006_rename_contact_userr_contact_remove_userr_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='user_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
