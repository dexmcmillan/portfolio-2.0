# Generated by Django 4.1.3 on 2022-11-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_project_publication"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="show",
            field=models.BooleanField(blank=True, default=True),
        ),
    ]