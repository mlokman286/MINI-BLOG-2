# Generated by Django 4.2.6 on 2023-10-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0003_post_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timing',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
