# Generated by Django 4.1.3 on 2022-11-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_job_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="publication",
            field=models.CharField(blank=True, max_length=40),
        ),
    ]