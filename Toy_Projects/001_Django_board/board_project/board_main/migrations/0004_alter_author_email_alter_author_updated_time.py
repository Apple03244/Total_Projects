# Generated by Django 4.2.2 on 2023-06-15 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board_main", "0003_alter_author_updated_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="updated_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
