# Generated by Django 3.2.15 on 2022-11-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='core.Image'),
        ),
    ]