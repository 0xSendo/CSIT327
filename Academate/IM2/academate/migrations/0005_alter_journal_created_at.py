# Generated by Django 5.1.1 on 2024-11-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academate', '0004_journal_updated_at_alter_journal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
