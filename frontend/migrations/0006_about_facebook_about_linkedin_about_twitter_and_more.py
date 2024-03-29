# Generated by Django 5.0.1 on 2024-01-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
