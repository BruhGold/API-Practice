# Generated by Django 5.1.6 on 2025-03-22 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_choice_question'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                "INSERT INTO api_question SELECT * FROM polls_question;",
                "INSERT INTO api_choice SELECT * FROM polls_choice;",
                "DROP TABLE polls_question;",
                "DROP TABLE polls_choice;"
            ],
        ),
    ]
